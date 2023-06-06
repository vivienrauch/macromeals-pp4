from .models import Comment, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message',)