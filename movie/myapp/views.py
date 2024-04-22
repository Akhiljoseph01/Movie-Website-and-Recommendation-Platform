from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from .models import Category
import requests
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Movie, Review, User
from myapp.models import Review
from django.http import HttpResponse
from .models import *
from myapp.forms import *

from .forms import ReviewForm

from django.contrib.auth.decorators import login_required

def category_summary(request):
    return render(request, 'category_summary.html', {'movies':Movie, 'category':category})


def category(request, foo):
	# Replace Hyphens with Spaces
	foo = foo.replace('-', ' ')
	# Grab the category from the url
	try:
		# Look Up The Category
		category = Category.objects.get(name=foo)
		movies = Movie.objects.filter(category=category)
		return render(request, 'category.html', {'movies':movies, 'category':category})
	except:
		messages.success(request, ("That Category Doesn't Exist..."))
		return redirect('home')



def search_view(request):
    # Check if the user has submitted a search query
    if 'q' in request.GET:
        search_query = request.GET['q']
        api_key = 'YOUR_OMDB_API_KEY'
        url = f'http://www.omdbapi.com/?apikey=fc96d6f7&s={search_query}'  # OMDB API endpoint for searching movies
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results = data.get('Search', [])  # Extract the search results from the response JSON
            return render(request, 'search_results.html', {'results': results})
        else:
            error_message = "Failed to retrieve search results. Please try again later."
            return render(request, 'search_results.html', {'error_message': error_message})
    else:
        # If no search query is provided, render the search form
        return render(request, 'search_results.html')



def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You have Registered Successfully!! WELCOME"))
            return redirect('home')
        else:
            messages.success(request,("Ooops.... There was a problem, Please try again!!"))
            return redirect('register')
            
    else:    
        return render(request, 'register.html', {'form':form})
    


def base(request):
    return render(request, 'base.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again..."))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})
    
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout
    
    

def home(request):
    # Logic to fetch movies from the database
    movies = Movie.objects.all()
    # Pass the movies to the template context
    return render(request, 'home.html', {'movies': movies})



def add_review(request, id):
    if request.user.is_authenticated:        
        movie = Movie.objects.get(id=id)
        print(movie.id)
        # review = Review.objects.filter(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                print("Valid")
                data = form.save(commit=False)
                # data = form.save()
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                # print(data)
                data.save()
                # return render(request, 'add_review.html', {"form": form})
                return redirect("movie_detail", id)
            else:
                form = ReviewForm()
        return render(request, 'add_review.html', {"form": form})
    else:
        return redirect("login")


# views.py



    
    
    
def movie_detail(request, movie_id):
    
    movie = get_object_or_404(Movie, pk=movie_id)
    # movie = Movie.objects.filter(id=id)
    reviews = Review.objects.filter(movie=movie_id)
    # print(movie)
    # print(reviews)
    context = {
        "movie":movie,
        "reviews":reviews
    }
    
    return render(request, 'movie_details.html', {'movie': movie, 'reviews': reviews})
    
    
        # else:
        #     return redirect("accounts:login")
            
            
    # reviews = Review.objects.filter(movie=movie)
    # return render(request, 'review.html', {'movie': movie, 'reviews': reviews})






# def review(request, movie_id):
#     # Logic to fetch reviews for a specific movie
#     movie = Movie.objects.get(pk=movie_id)
#     reviews = Review.objects.filter(movie=movie)
#     return render(request, 'review.html', {'movie': movie, 'reviews': reviews})

def user(request, user_id):
    # Logic to fetch user details and their reviews
    user = User.objects.get(pk=user_id)
    reviews = Review.objects.filter(user=user)
    return render(request, 'user.html', {'user': user, 'reviews': reviews})

def about(request):
    return render(request, 'about.html', {})

# def Rate(request, movie_id):
#     movie =Movie.objects.get(movieID=movie_id)
#     user = request.user
    
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.movie = movie
            rate.save()
            return HttpResponseRedirect(reverse('movie-details, args=[movie_id]'))
        else:
            form = RateForm()
            