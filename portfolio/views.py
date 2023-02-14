from django.shortcuts import render
from .models import Project
# Create your views here. #render conoce la carpeta templates comentario
def home(request):
    projects =  Project.objects.all() #proyectos en la base de datos
    return render(request,'home.html', {'projects':projects})