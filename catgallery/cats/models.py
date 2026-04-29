from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='cats/', blank=True, null=True)
    adopted_on = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
