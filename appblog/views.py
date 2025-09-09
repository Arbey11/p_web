from django.shortcuts import render
from appblog.models import Categorias, Post

# Create your views here.

def blog(request):
    cat = Categorias.objects.all()
    pst = Post.objects.all()
    return render(request, "appblog/blog.html", {'categoria':cat, 'post':pst}) 


def categoria(request, categorias_id):
    ctg = Categorias.objects.get(id=categorias_id)
    post = Post.objects.filter(relacion_categorias=ctg)
    return render(request, "appblog/categoria.html", {'categoria':ctg, 'posts':post})    


