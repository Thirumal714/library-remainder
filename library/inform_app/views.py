from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def reader(request):
    return render(request,'templatesapp/book.html')
