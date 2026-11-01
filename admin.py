from django.contrib import admin
from .models import Book, Student, SeatBooking, Attendance, Payment
admin.site.register([Book, Student, SeatBooking, Attendance, Payment])
