from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm,NameForm,ArticleForm,BlogForm,AuthorForm
from .models import Blog,Article,Person,Author
from django.urls import reverse_lazy
from django.views.generic.edit import FormView,CreateView, DeleteView, UpdateView
# Create your views here.

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name','age']
    template_name='author.html'
    initial={'name':'xxxx','age':11}
    success_url='/app1/{slug}/success/'
    # queryset=Author.objects.all()
    

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
    template_name = 'contact.html'
    form_class = ContactForm
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
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            data=form.cleaned_data
            print('post')
            a=Author(name=data['name'],age=data['age'])
            a.save()
            for x in Author.objects.all().values():
                print(x)
            # Article(title=data['title'],content=data['content'],blog=data['blog'],file=data['file']).save()
            # redirect to a new URL:
            return HttpResponseRedirect(a.get_absolute_url())

    # if a GET (or any other method) we'll create a blank form
    else:
        print('get')
        form = AuthorForm()

    return render(request, 'author.html', {'form': form})

def thanks(request):
    return HttpResponse('thank you')