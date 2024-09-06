from rest_framework import serializers
from .models import Author, Book
# BookSerializer handles serialization of Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
    
    # Includes custom validation to ensure publication_year is not in future 
    def validate_publication_year(self, value):
        import datetime
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future !")
        return value

# AuthorSerializer handles serialization of Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to display related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
    