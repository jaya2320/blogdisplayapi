from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'index.html',{'response':response})