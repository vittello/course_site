from django import forms
from .models import Course
from .models import Comment

class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['slug', 'title', 'desc', 'image']
        
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'lesson']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.HiddenInput(),
            'lesson': forms.HiddenInput(),
        }
        
        labels = {
            'text': 'Сообщение*'
        }
    