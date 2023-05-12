from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import MovieForm

# Create your views here.
def Movie(request):
    movies = movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html', context)

def details(request,ID):
    movies = movie.objects.get(id=ID)
    return render(request,'details.html', {'movies':movies})

def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        img = request.FILES['img']
        movies=movie(name=name, disc=desc, year=year , rateing=rating, img=img)
        movies.save()

    return render(request,'add.html')

def update(request,ID):
    movies=movie.objects.get(id=ID)
    form=MovieForm(request.POST or None, request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html', {'form':form,'movies':movies})
def delet(request,ID):
    if request.method=='POST':
        movies=movie.objects.get(id=ID)
        movies.delete()
        return redirect('/')
    return render(request,'delet.html')