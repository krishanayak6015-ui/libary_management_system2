from django.conf import settings
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    category = models.CharField(max_length=80, blank=True)
    isbn = models.CharField(max_length=30, blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} — {self.author}"

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    course = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.get_full_name() or self.user.username

class SeatBooking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=20)
    booking_date = models.DateField()
    status = models.CharField(max_length=20, default="Booked")
    def __str__(self):
        return f"{self.seat_number} - {self.booking_date}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10, choices=[("Present","Present"),("Absent","Absent")], default="Present")
    class Meta:
        unique_together = ("student", "attendance_date")

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_date = models.DateField()
    purpose = models.CharField(max_length=120, default="Library fee")
    status = models.CharField(max_length=20, default="Paid")
    def __str__(self):
        return f"{self.student} - {self.amount}"
