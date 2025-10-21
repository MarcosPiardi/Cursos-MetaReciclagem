from django.shortcuts import render
from .models import Curso  # ajuste conforme seu modelo

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursoseoutros/lista_cursos.html', {'cursos': cursos})
