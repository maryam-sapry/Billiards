from django.shortcuts import render



def home(requset):
    return render(requset, 'pages/home.html')
# Create your views here.
