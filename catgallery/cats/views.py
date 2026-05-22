from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import connection
from .models import Cat
from blog.models import Post


def gallery(request):
    cats = Cat.objects.all()
    recent_posts = Post.objects.filter(published=True)[:4]
    return render(request, 'cats/gallery.html', {'cats': cats, 'recent_posts': recent_posts})


def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'cats/cat_detail.html', {'cat': cat})


def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "ok"})
    except Exception as e:
        return JsonResponse({"status": "error", "error": str(e)}, status=500)
