from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people']
        widgets = {
            
            'date': forms.SelectDateWidget(),
            'time': forms.Select(choices=Booking.TIME_CHOICES), 
            'number_of_people': forms.Select(choices=Booking.NUMBER_OF_PEOPLE_CHOICES)
        }
