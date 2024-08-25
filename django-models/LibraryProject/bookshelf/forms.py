from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if '<script>' in title:
            raise forms.ValidationError("Invalid title - scripts are not allowed.")
        return title
    

    from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if '<script>' in message:
            raise forms.ValidationError("Invalid message - scripts are not allowed.")
        return message