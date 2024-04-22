from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import settings
from django.conf.urls.static import static
from myapp.views import home  # Import the home view from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('', include('myapp.urls')),
    path('watchlist/', include('watchlist.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)