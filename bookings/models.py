from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()

    TIME_CHOICES = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(17, 22) for minute in range(0, 60, 15)]
    time = models.CharField(max_length=5, choices=TIME_CHOICES)

    NUMBER_OF_PEOPLE_CHOICES = [(i, i) for i in range(1, 11)] 
    number_of_people = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.name


