from django import forms
from .models import Booking, Review, Delivery
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):
    email =forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'custom_name', 'check_in_date', 'check_out_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['country', 'first_name', 'last_name', 'address', 'phone']