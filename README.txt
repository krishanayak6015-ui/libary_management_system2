LIBRIFY - DJANGO LIBRARY MANAGEMENT SYSTEM
==========================================

REQUIREMENTS
- Python 3.12 or newer
- Internet connection for Bootstrap CDN (optional; pages still work without it)

RUN ON WINDOWS
1. Extract the ZIP file.
2. Open the extracted LibraryManagement_Django folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:
   py -m venv venv
5. Activate it:
   venv\Scripts\activate
6. Install packages:
   py -m pip install -r requirements.txt
7. Create database tables:
   py manage.py makemigrations
   py manage.py migrate
8. Create admin login:
   py manage.py createsuperuser
9. Start website:
   py manage.py runserver
10. Open http://127.0.0.1:8000/

PAGES
- Home, Signup, Login, Logout
- Dashboard
- Book list, search and add book
- Student records
- Seat booking records
- Attendance records
- Payment records
- Django admin at /admin/

HOW TO ADD STUDENT / SEAT / ATTENDANCE / PAYMENT DATA
Login to /admin/ using your superuser account. Add Student first (link it to a user),
then add seat bookings, attendance and payments.

DATABASE
This starter project uses SQLite for easy local setup. The SQLite database file is
created automatically after running migrations.

IMPORTANT DEPLOYMENT NOTE
This package is configured for local development, not one-click Vercel deployment.
SQLite files on serverless hosting may not persist. For production, use a hosted
PostgreSQL database, set DEBUG=False, configure ALLOWED_HOSTS and
CSRF_TRUSTED_ORIGINS for your real domain, and use environment variables for
SECRET_KEY and database credentials. Do not deploy with DEBUG=True or the sample
SECRET_KEY.
