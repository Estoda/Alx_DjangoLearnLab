# Advanced API Project

This project demonstrates the implementation of a REST API using Django REST Framework (DRF). It includes custom views built with DRF's generic views and mixins to handle CRUD operations for the `Book` model.

## Features
- List all books
- Retrieve details of a specific book
- Create a new book (restricted to authenticated users)
- Update a book (restricted to authenticated users)
- Delete a book (restricted to authenticated users)
- Permission-based access control

## Endpoints

### 1. List All Books
- **URL**: `/books/`
- **Method**: `GET`
- **Description**: Retrieves a list of all available books.
- **Access**: Open to all users (unauthenticated access allowed).

### 2. Retrieve a Single Book
- **URL**: `/books/<int:pk>/`
- **Method**: `GET`
- **Description**: Retrieves the details of a book by its ID (`<int:pk>`).
- **Access**: Open to all users (unauthenticated access allowed).

### 3. Create a New Book
- **URL**: `/books/create/`
- **Method**: `POST`
- **Description**: Adds a new book to the database. Only authenticated users can create books.
- **Request Body** (example):
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "published_date": "2024-01-01"
  }
