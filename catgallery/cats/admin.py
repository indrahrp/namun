from django.contrib import admin
from .models import Cat

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'adopted_on')
    search_fields = ('name', 'breed')
