import uuid
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def readmore(request):
    return render(request, 'get_out.html')

def singup(request):

    if request.method == "POST":
        form = login_form(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Walcome back!")
                auth.login(request, user)
                return redirect('home')
        else:
            messages.warning(request, "Your username or password is incorrect!")
    form = login_form()

    context = {'form':form}
    return render(request, 'user/singup.html', context)

def register(request):

    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered! Now you can Sing Up!")
            return redirect('singup')
    else:
        form = register_form()
    context = {'form': form}

    return render(request, 'user/register.html', context)

def logout(request):
    messages.info(request, "You are logout!")
    auth.logout(request)
    return  render(request, 'home.html')

def galery(request):
    return render(request, 'galery.html')

@login_required(login_url='singup')
def book(request):
    if request.method == 'POST':
        check = True
        select = request.POST['select']
        depart = request.POST['depart']
        returning = request.POST['returning']
        adults = request.POST['adults']

        if check != '' and select !='' and depart != '' and returning != '' and adults != '' :
            bookings = Booking(travel_roundtrip=check, travel_city=select, travel_departing=depart, travel_returing=returning, travel_adults=adults, user=request.user)
            bookings.save()
            return redirect('flight', pk=bookings.travel_id, country_2=select)

    return render(request, 'book.html')


def flight(request, pk, country_2):
    current_datetime = timezone.now()
    flights = Flight.objects.filter(country_2=country_2)

    # Filter bookings with a departure date greater than the current date
    bookings = Booking.objects.filter(pk=pk, travel_departing__gte=current_datetime.date())

    # Create an empty list to store valid bookings
    valid_bookings = []

    for booking in bookings:
        if booking.travel_departing == current_datetime.date() and booking.travel_flight:
            # If departure date is today and travel_flight is not None, check departure time
            departure_time = timezone.make_aware(
                timezone.datetime.combine(
                    current_datetime.date(),
                    booking.travel_flight.time
                )
            )
            if departure_time > current_datetime:
                # Only add if departure time is in the future
                valid_bookings.append(booking)
        elif booking.travel_departing > current_datetime.date():
            # If departure date is in the future, add it
            valid_bookings.append(booking)

    if not valid_bookings:
        # Handle the case where no valid bookings are found
        messages.warning(request, 'Sorry, we dont have any flights on that day!')
        return redirect('book')

    context = {'flights': flights, 'booking': valid_bookings[0]}
    return render(request, 'show_flight.html', context)



def pay(request, booking, flight):
    flights = Flight.objects.all()
    flight = Flight.objects.get(pk=flight)
    booking = Booking.objects.get(pk=booking)
    booking.travel_flight = flight
    booking.save()
    total = booking.total_price

    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': booking.pk,
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal_return")}',
        'cancel_return': f'http://{host}{reverse("paypal_cancel")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)

    context = {'flight': flight, 'booking': booking, 'form':form, 'flights':flights, 'total':total}
    return render(request, 'pay.html', context)


def paypal_return(request):
    return redirect("success")

def paypal_cancel(request):
    messages.warning(request, 'Your ticket has not been paid! You only send the flight reservation! To pay you have to start again from the beginning!')
    return redirect("home")

def success(request):
    return render(request, 'payment_success.html')
