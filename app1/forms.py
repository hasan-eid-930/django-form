from django import forms
from .models import Article,Blog,Author
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [ 'subject']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'title','content','file','blog']
    
class NameForm(forms.Form):
    name = forms.CharField(max_length=45)
    file=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class AuthorForm(forms.ModelForm):
    class Meta:
       model=Author
       fields=['name','age']
        
class ContactForm(forms.Form):
    name = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print(self.cleaned_data)
        print('send')
        pass