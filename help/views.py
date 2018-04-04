from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    help_dic = {'help_title':"How to?",'help':"Be yourself"}

    return render(response,'help/index.html',context=help_dic)