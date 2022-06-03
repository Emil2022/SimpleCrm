from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def index(request):
    # return HttpResponse('Hello!') # -> This outputs the string Hello!
    return render(request, 'SimpleCrm/base.html') # -> This renders information from index.html
    # Render takes in 3 parameters: 
        # 1. request from the view function 
        # 2. The name of the html file 
        # 3. A dictionary of string to any value -> Values on the left side of the colon can be used in html code

def login(request):
    return render(request,'login.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/sheet')
    
    else:
        form = RegisterForm()
    return render(request, '/sign_up.html', {"form": form})

def sheet(request):
    return render(request, 'sheet.html')

# VIEWS NOTES:
# Create your views here.
# View functions take in requests and return responses
# This is a request handler / action / view (Not to be confused with what is seen by the user (Template))