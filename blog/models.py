from django.db import models #""" lineas para añadir algo de otros archivos, para no copiar y pegar """
from django.utils import timezone

class Post(models.Model): #"""esta linea dice que estamos definiendo un objeto/ class=palabra clave para objeto; 
							#post/ nombre del objeto; models.Model/ significa que Post es un objeto de Django, asi 
							#Django sabe que debe guardarlo en una base de datos  """

	author = models.ForeignKey('auth.User') #"""esto es un vinculo con otro modelo """
	title = models.CharField(max_length=200) #"""esto es como defines un texto con un numero limitado de caracteres"""
	text = models.TextField() #"""esto es como defines textos largos sin limites"""
	created_date = models.DateTimeField( #"""esto es fecha y hora """
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True) 

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title