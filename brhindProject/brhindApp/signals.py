from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received

from .models import *

@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    print('Ipn valid')
    ipn = sender
    if ipn.payment_status == 'Completed':
        if ipn.receiver_email != "joni10@gmail.com":
            print('Invalid receiver email:', ipn.receiver_email)
            return
        if ipn.receiver_email == "joni10@gmail.com":
            my_pk = ipn.item_name
            booking = Booking.objects.get(pk=my_pk)
            booking.ticket_is_paid = True
            booking.save()
