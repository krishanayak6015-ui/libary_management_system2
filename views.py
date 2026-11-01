from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Book, Student, SeatBooking, Attendance, Payment

def home(request):
    return render(request, "main/home.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        if not username or not password:
            messages.error(request, "Username and password are required.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "That username is already taken.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect("dashboard")
    return render(request, "main/signup.html")

def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    return render(request, "main/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    return render(request, "main/dashboard.html", {
        "book_count": Book.objects.count(),
        "student_count": Student.objects.count(),
        "booking_count": SeatBooking.objects.filter(booking_date=date.today()).count(),
        "payment_count": Payment.objects.count(),
        "recent_books": Book.objects.order_by("-created_at")[:5],
    })

@login_required
def books(request):
    q = request.GET.get("q", "")
    items = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q)) if q else Book.objects.all()
    return render(request, "main/books.html", {"books": items.order_by("title")})

@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        if title and author:
            total = int(request.POST.get("total_copies") or 1)
            Book.objects.create(title=title, author=author, category=request.POST.get("category",""),
                                isbn=request.POST.get("isbn",""), total_copies=total, available_copies=total)
            messages.success(request, "Book added successfully.")
            return redirect("books")
        messages.error(request, "Title and author are required.")
    return render(request, "main/add_book.html")

@login_required
def students(request):
    return render(request, "main/students.html", {"students": Student.objects.select_related("user").all()})

@login_required
def seats(request):
    return render(request, "main/seats.html", {"bookings": SeatBooking.objects.select_related("student","student__user").order_by("-booking_date")})

@login_required
def attendance(request):
    return render(request, "main/attendance.html", {"records": Attendance.objects.select_related("student","student__user").order_by("-attendance_date")})

@login_required
def payments(request):
    return render(request, "main/payments.html", {"payments": Payment.objects.select_related("student","student__user").order_by("-payment_date")})
