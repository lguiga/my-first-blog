from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	# Cria um QuerySet com uma lista dos posts ordenados pela data
	return render(request, 'blog/post_list.html', {})
