from relationship_app.models import Author, Book, Librarian, Library

books = Book.objects.all()
for book in books:
    if book.author.name == "Ahmed Amin":
        print(book.title)

library = Library.objects.get(name = "Alex")
books = library.books.all()

for book in books:
    print(book.title)

for l in Librarian.objects.all():
    if l.Library.name == "Cairo":
        print(l.name)

