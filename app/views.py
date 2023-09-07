from django.shortcuts import render
from django.http import HttpResponse
from . forms import ContactForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def service(request):
    return render(request,'404.html')

def news(request):
    return render(request,'news.html')

def mail(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form' : form}
    return render(request, 'mail.html', context=context) 

def single(request):
    return render(request, 'single.html')

