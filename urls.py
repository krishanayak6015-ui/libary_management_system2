from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("books/", views.books, name="books"),
    path("books/add/", views.add_book, name="add_book"),
    path("students/", views.students, name="students"),
    path("seats/", views.seats, name="seats"),
    path("attendance/", views.attendance, name="attendance"),
    path("payments/", views.payments, name="payments"),
]
