from django.shortcuts import render
from . models import Book, Author, BookInstance, Genre
# Create your views here.
def index(request):
	#Generar contadores de algunos objetos.
	num_books= Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	#Libros disponibles (estado='a')
	num_Instances_avaible = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count() #All implicito por defecto


	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_Instances_avaible':num_Instances_avaible,'num_authors':num_authors},
		)