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


## API Features
- **Filtering**: You can filter books by `title`, `author`, and `publication_year`.
  - Example: `/books/?author__name=John`
- **Search**: You can search for books by `title` or `author`.
  - Example: `/books/?search=Python`
- **Ordering**: You can order books by `title` or `publication_year`.
  - Example: `/books/?ordering=title`


## Testing
We have implemented unit tests for the following scenarios:
- **CRUD Operations**: Tested creation, retrieval, updating, and deletion of Books.
- **Filtering, Searching, and Ordering**: Verified these functionalities work as expected.
- **Authentication/Permissions**: Ensured proper access control.

To run the tests:
```bash
python manage.py test api
