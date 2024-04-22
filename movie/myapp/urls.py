# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('search/', views.search_view, name='search'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this line for the logout URL
    path('register/', views.register_user, name='register'),
    path('about/', views.about, name='about'),
    # path('', views.home, name='home'),
    # path('movie/<int:id>/', views.Movie, name='movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('addreview/<int:id>/', views.add_review, name='add_review'),
    path('category/<str:foo>/', views.category, name='category'),

]