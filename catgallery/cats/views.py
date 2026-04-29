from django.shortcuts import render, get_object_or_404
from .models import Cat


def gallery(request):
    cats = Cat.objects.all()
    return render(request, 'cats/gallery.html', {'cats': cats})


def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'cats/cat_detail.html', {'cat': cat})
