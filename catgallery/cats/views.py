from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import connection
from .models import Cat
from blog.models import Post

CATS = [
    {"name": "Timothy",  "img": "cats/img/timothy.png",  "role": "The Sunbather",  "blurb": "Lord of the patio chair. Will judge you gently with one eye open."},
    {"name": "Chia",     "img": "cats/img/chia.png",     "role": "The Lounger",    "blurb": "Professional napper, part-time floof. Has never once been in a hurry."},
    {"name": "Mooi",     "img": "cats/img/mooi.png",     "role": "The Diva",       "blurb": "Fluffiest of them all and she knows it. Poses like the camera owes her."},
    {"name": "Balinese", "img": "cats/img/balinese.png", "role": "The Flower Girl","blurb": "Wears a frangipani like a crown. Poolside royalty, all day long."},
    {"name": "Lolla",    "img": "cats/img/lolla.png",    "role": "The Watcher",    "blurb": "Keeps an eye on the whole street from her sunny window throne."},
    {"name": "Puji",     "img": "cats/img/puji.png",     "role": "The Sweetheart", "blurb": "Big green eyes, even bigger heart. Flops over for belly rubs on sight."},
    {"name": "Leo",      "img": "cats/img/leo.png",      "role": "The Gentleman",  "blurb": "Wears his lucky-cat charm with pride. Soft, regal, a little dramatic."},
    {"name": "Rescued",  "img": "cats/img/rescued.png",  "role": "The Newest One", "blurb": "Found, loved, and never letting go again. Our happiest ending."},
    {"name": "Chloe",    "img": "cats/img/chloe.png",    "role": "The Queen",      "blurb": "Permanently unimpressed Persian. Rules the house with one fluffy paw."},
    {"name": "Bellaa",   "img": "cats/img/bellaa.png",   "role": "The Beauty",     "blurb": "Ocean-blue eyes and a little green bell. Elegant down to her toe beans."},
]

GALLERY = [
    {"img": "cats/img/mooi-belly.png",    "cap": "Mooi, mid-dream"},
    {"img": "cats/img/leo.png",           "cap": "Sir Leo"},
    {"img": "cats/img/puji.png",          "cap": "Puji says hi"},
    {"img": "cats/img/balinese.png",      "cap": "Flower girl Balinese"},
    {"img": "cats/img/mooi-printer.png",  "cap": "Mooi claims the printer"},
    {"img": "cats/img/chia.png",          "cap": "Chia, unbothered"},
    {"img": "cats/img/lolla.png",         "cap": "Lolla on watch"},
    {"img": "cats/img/leo-walk.png",      "cap": "Leo on patrol"},
    {"img": "cats/img/bellaa.png",        "cap": "Bellaa lounging"},
    {"img": "cats/img/chloe.png",         "cap": "Queen Chloe"},
    {"img": "cats/img/timothy.png",       "cap": "Timothy soaking up sun"},
    {"img": "cats/img/leo-portrait.png",  "cap": "Leo, up close"},
]


def gallery(request):
    return render(request, 'cats/gallery.html', {
        'cats': CATS,
        'gallery_items': GALLERY,
    })


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
