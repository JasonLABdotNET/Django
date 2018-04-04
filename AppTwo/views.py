from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(hello):
   my_dict = {'insert_me':"hello, I'm from heavn"}
   return render(hello, 'first_app_temp/index.html', context = my_dict)
