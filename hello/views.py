from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	html = "<html><body><title>Учим django</title><h1>Добро пожаловать</h1><a href='/hello/about'>О нас</a></body></html>"
	return HttpResponse(html)

def about(request):
	html = "<html><body><title>О нас</title><h1>Ковальчук Владимир</h1><a href='/hello'>Главная страница</a></body></html>"
	return HttpResponse(html)