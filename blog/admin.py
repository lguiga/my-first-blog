from django.contrib import admin
from .models import Post

# Register your models here.

# Registra o modelo para que possamos ver na página de administrador
admin.site.register(Post)
