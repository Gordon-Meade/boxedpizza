from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

def booking_view(request):
    # Logic for handling booking view
    return render(request, 'booking.html')

    
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/book_table.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

@login_required
def booking_details(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'booking_details.html', {'booking': booking})

