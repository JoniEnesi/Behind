from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("readmore", views.readmore, name="readmore"),
    path("singup", views.singup, name="singup"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("galery", views.galery, name="galery"),
    path("book", views.book, name="book"),
    path("flight/<int:pk>/<str:country_2>/", views.flight, name="flight"),
    path("pay/<int:booking>/<int:flight>", views.pay, name="pay"),
    path("paypal_return", views.paypal_return, name="paypal_return"),
    path("paypal_cancel", views.paypal_cancel, name="paypal_cancel"),
    path("success", views.success, name="success"),
]