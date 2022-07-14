from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Cat
from .forms import FeedingForm 
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Faux Cat Data - Database simulation

#class Cat:
    #self.name = name
     #self.breed = breed
     #self.description = description
     #self.age = age


#cats = [
  #Cat('Lolo', 'tabby', 'foul little demon', 3),
  #Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  #Cat('Raven', 'black tripod', '3 legged cat', 4)
#]


# Create your views here.

def home(request):
    return HttpResponse('<h1>Hola Mundo /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    #if you want to send back raw text or an html string use httpresponse
    #if you want to send back a full template file use render 
    #return HttpResponse('<h1>About the CatCollector</h1>')
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
    # Get the individual cat 
  cat = Cat.objects.get(id=cat_id)
  # instantiate our feeding form 
  feeding_form = FeedingForm()
  # render template, pass it the cat 
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form': feeding_form })

def add_feeding(request, cat_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'
