from django.db import models
# Author model represents an author with a name field
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# an author can have multiple books (one-to-many relationship)
# Book model represents a book with title, publication year, a foreign key to author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField(default=2000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Books')

    def __str__(self):
        return self.title

