
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # author = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=Post
        fields=('author','title')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Login'}),
            'author':forms.PasswordInput(attrs={'class':'form-control input-lg','placeholder':'Mot de pass'})
        }