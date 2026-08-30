from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, request
from Hamilton.forms import NameForm, contactForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'exelent!!!!!')
        else:
          messages.add_message(request,messages.ERROR,'noooooooo!!!!!')  
    form = contactForm()
        
    return render(request,'website/contact.html', {'form': form})



