from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

MAX_SEATS = 20

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()

    TIME_CHOICES = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(17, 22) for minute in range(0, 60, 30)]
    time = models.CharField(max_length=5, choices=TIME_CHOICES)

    NUMBER_OF_PEOPLE_CHOICES = [(i, i) for i in range(1, 11)] 
    number_of_people = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.name

    def clean(self):
        # Check if there are available seats for the given date and time
        if self.pk is None:  # This is a new booking being added
            existing_bookings = Booking.objects.filter(date=self.date, time=self.time)
            total_people_booked = sum(booking.number_of_people for booking in existing_bookings)
            total_people_booked += self.number_of_people  # Include the current booking
            if total_people_booked > MAX_SEATS:
                raise ValidationError("Not enough seats available for this date and time.")

    class Meta:
        unique_together = ('date', 'time')  # Ensure no double booking for the same date and time
