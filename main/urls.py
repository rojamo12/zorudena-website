from django.urls import path  # ✅ include is now imported
from . import views

urlpatterns = [
    path('', views.home, name='home'),                           # Homepage
    path('contact/', views.contact, name='contact'),       # Contact page
    path('about/', views.about_us, name='about_us'),             # About page
    path('blog/', views.blog, name='blog'),                         # Include blog app's URLs
    path('programs/', views.programs, name='programs'),          # Programs page
    path('blog/category/<str:category>/', views.blog_by_category, name='blog_by_category'),  # Blog category filter
]
