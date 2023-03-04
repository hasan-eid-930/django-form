from django.db import models
from django.urls import reverse
from django.core import validators
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
# Create your models here.
sub_choices=[
    ('s1','subject 1'),
    ('s2','subject 2'),
    ('s3','subject 3'),
]
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
def get_blog():
    return Blog.objects.filter(subject='s3')[0]

class Blog(models.Model):
    subject=models.CharField(max_length=50,choices=sub_choices,blank=False,default='s2')

    def __str__(self) -> str:
        return self.subject 

class Article(models.Model):
    title=models.CharField(max_length=50,null=True)
    content=models.TextField()
    file=models.FileField(upload_to='uploaded_files',null=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True,default=get_blog)
   
    def __str__(self) -> str:
        return self.title  
  
class Person(models.Model):
    name=models.CharField(max_length=50,null=True)
    file=models.FileField(upload_to='uploaded_files')

    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    age=models.IntegerField(default=25)
    slug=AutoSlugField(unique=True,populate_from='name',editable=True,default='xc', always_update=True)
    def get_absolute_url(self):
        return reverse('author-delete', kwargs={'pk': self.pk}) 
    
    # def save(self, **kwargs):
    #     self.slug = slugify(self.name)
    #     print('save')
    #     super().save(**kwargs)