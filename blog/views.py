from django.shortcuts import render
from django.utils import timezone
from .models import Post #"""El punto después de from indica el directorio actual o la aplicación actual. 
from django.shortcuts import render, get_object_or_404 #Como views.py y models.py están en el mismo directorio, simplemente usamos . y el nombre del archivo (sin .py).
#Ahora importamos el nombre del modelo (Post)."""

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})