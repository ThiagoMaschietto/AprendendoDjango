from django.shortcuts import render, get_object_or_404
from .models import Imagen

# Create your views here.

def home(request):
    imagens = reversed(Imagen.objects.all())
    return render(request, 'base.html', {'imagens':imagens})

def detalhes_post(request, nome):
    post = get_object_or_404(Imagen, nome = nome)
    return render(request, 'saibamais.html', {'post': post})
