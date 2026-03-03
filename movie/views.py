from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from collections import Counter
import matplotlib
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def home(request):
    searchTerm = request.GET.get('searchMovie')
    
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {
        'movies': movies
    })


def about(request):
    return render(request, 'about.html')


def movies_by_year_chart(request):

    movies = Movie.objects.all()

    years = [movie.year for movie in movies if movie.year]

    counter = Counter(years)

    years_sorted = sorted(counter.keys())
    counts = [counter[year] for year in years_sorted]

    plt.figure()
    plt.bar(years_sorted, counts)
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.title("Movies by Year")

    response = HttpResponse(content_type="image/png")
    plt.savefig(response, format="png")
    plt.close()

    return response


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {
        'email': email
    })
    
def statistics_page(request):
    return render(request, 'statistics.html')