from django.shortcuts import render, redirect

from .forms import Movieform
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {'movie': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, "add.html")


def update_movie(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html", {'form': form, 'movie': movie})

def delete_movie(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")





    # def delete_movie(request, id):
    #     if request.method == 'POST':
    #         movie = Movie.objects.get(id=id)
    #         movie.delete()
    #         return redirect('/')
    #     return render(request, "delete.html")
# Create your views here.
# Fetch all datas from table
# def base(request):
#     movies = Movie.objects.all()
#     return render(request, "page1.html", {'movie': movies})
#
#
# # Fetch data from table using id
# def page2(request, movie_id):
#     movie = Movie. objects.get(id=movie_id)
#     return render(request, "page2.html", {'movie': movie})
#
#
# # Add new data to the table
# def page3(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         desc = request.POST.get('desc')
#         year = request.POST.get('year')
#         img = request.FILES['img']
#         movie = Movie(name=name, desc=desc, year=year, img=img)
#         movie.save()
#     return render(request, "page3.html")
#
#
# # Update datas using id
# def page4(request, id):
#     movie = Movie.objects.get(id=id)
#     form = Movieform(request.POST or None, request.FILES or None, instance=movie)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, "page4.html", {'form': form, 'movie': movie})
#
#
# # delete data using id
# def page5(request, id):
#     if request.method == 'POST':
#         movie = Movie.objects.get(id=id)
#         movie.delete()
#         return redirect('/')
#     return render(request, "page5.html")

# def index(request):
#     movies = Movie.objects.all()
#     return render(request, "index.html", {'movie': movies})
#
#
# def detail(request, movie_id):
#     movie = Movie.objects.get(id=movie_id)
#     return render(request, "detail.html", {'movie': movie})
