from django.shortcuts import render
from django.utils import timezone
from .models import Post #"""El punto después de from indica el directorio actual o la aplicación actual. 
from django.shortcuts import render, get_object_or_404 #Como views.py y models.py están en el mismo directorio, simplemente usamos . y el nombre del archivo (sin .py).
from .forms import PostForm #Ahora importamos el nombre del modelo (Post)."""
from django.shortcuts import redirect

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):

	#if request.method == "POST":

		form = PostForm(request.POST)
		if form.is_valid():
				post = form.save(commit=False) #author es obligatorio
				post.author = request.user
				post.published_date = timezone.now()
				post.save() # guardar formulario 
				return redirect('blog.views.post_detail', pk=post.pk) # post recien creado, 'blog.views.. es el nombre de la vista donde queremos ir'
		else:
			form = PostForm()

		return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

