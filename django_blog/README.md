## Authentication System

This document provides an overview of the user authentication system implemented in the blog project.

### Features:
- User registration
- User login and logout
- Profile management

### Setup Instructions:
1. Register a new user by visiting `/register`.
2. Log in at `/login`.
3. Access the profile page at `/profile`.

### Security:
- CSRF protection is enabled on all forms.
- Passwords are stored securely using Django's hashing algorithm.
