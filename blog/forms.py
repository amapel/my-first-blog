from django import forms #importando forms
from .models import Post

class PostForm(forms.ModelForm): #postForm= es el nombre del formulario que es un ModelForm

    class Meta:         #indica el modelo para realizar el formulario => model = post
            model = Post
            fields = ('title', 'text',) #dentro del parentesis colocamos los campos que deseamos en el formulario