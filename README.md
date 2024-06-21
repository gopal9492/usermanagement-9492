# User Management System

This is a Django-based web application for user management. The system allows users to sign up, log in, edit their profiles, and log out. Additionally, there is an admin interface for managing users, including editing and deleting user accounts.

## Features

- User Signup
- User Login
- User Profile View and Edit
- User Logout
- Admin Login
- Admin User Management (View, Edit, Delete Users)

## Prerequisites

- Python 3.12
- Django 

1. **User Signup:**
    - Navigate to the Signup page (`/signup/`) and fill in the required information.
    - If the username is unique, the user will be registered and redirected to the signup success page.

2. **User Login:**
    - Navigate to the Login page (`/login/`) and enter the username and password.
    - If the credentials are correct, the user will be logged in and redirected to their profile page.

3. **Edit Profile:**
    - While logged in, navigate to the Edit Profile page (`/editprofile/`) to update personal information.

4. **Admin Management:**
    - Navigate to the Admin Login page (`/login_admin/`) and enter the admin credentials.
    - After logging in, the admin can manage users via the Manage Users page (`/manage_users/`).
