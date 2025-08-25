from django.contrib import admin
from django.urls import path
from . import views  # This should work now that we've created views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),  # Add this line
    path('blog/', views.blog, name='blog'),  # Add this line
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/archive/', views.blog_archive, name='blog_archive'),
    path('scripts/', views.scripts, name='scripts'),
    path('contact/', views.contact, name='contact')
]

