from django.shortcuts import render

def home (request):
    return render (request, 'index.html')

def login (request):
    return render (request, 'login.html')

def quem_somos (request):
    return render (request, 'quemsomos.html')

def disciplinas (request):
    return render (request, 'disciplinas.html')