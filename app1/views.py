from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm,NameForm,ArticleForm,BlogForm,AuthorForm,PersonForm
from .models import Blog,Article,Person,Author,Image
from django.urls import reverse_lazy
from django.views.generic.edit import FormView,CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.conf import settings
import os
from pathlib import Path
from django.http import FileResponse

# Create your views here.

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name','age']
    template_name='author.html'
    initial={'name':'xxxx','age':11}
    success_url='/app1/{slug}/success/'
    # queryset=Author.objects.all()

class PersonCreateView(FormView):
    # model = Person
    # fields = ['name','file']
    form_class=PersonForm
    template_name='name.html'
    success_url='/app1/thanks'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES.getlist('images')
        if form.is_valid():
            data=form.cleaned_data
            p=Person(name=data['name'])
            p.save()
            for img in images:
                print(img)
                Image(image=img,person=p).save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
class AuthorUpdateView(UpdateView):
    template_name='author_form.html'
    model = Author
    fields = ['name']

class AuthorDeleteView(DeleteView):
    model = Author
    template_name='author_confirm_delete.html'
    success_url = reverse_lazy('thanks')

def success(request,slug):
    a=Author.objects.get(slug=slug)
    print(a.name)
    print(a.age)
    return HttpResponse(slug)

def author_detail(request,pk):
    a=Author.objects.get(pk=pk)
    print(a.name)
    return HttpResponse('author details')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/app1/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

class NameFormView(FormView):
    form_class = NameForm
    template_name = 'name.html'  # Replace with your template.
    success_url = '/app1/thanks/'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                print(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            data=form.cleaned_data
            images = request.FILES.getlist('images')
            p=Person(name=data['name'])
            p.save()
            for img in images:
                Image(image=img,person=p).save()
            print('post')
            # redirect to a new URL:
            return HttpResponseRedirect('/app1/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('get')
        form = PersonForm()

    return render(request, 'name.html', {'form': form})

def download(request,pk):
    x=Person.objects.get(pk=pk)
    return FileResponse(x.file, as_attachment=True)
    
# class PersonListView(ListView):
#     model=Person
#     template_name='download.html'
#     context_object_name='persons'

def thanks(request):
    persons=Person.objects.all()
    # p=Person.objects.get(name='hasan3')
    return render(request,template_name='download.html',context={'persons':persons})

def person_details(request,name):
    person=Person.objects.get(name=name)
    images=Image.objects.filter(person=person)
    return render(request,'person_details.html',context={'person':person,'images':images})