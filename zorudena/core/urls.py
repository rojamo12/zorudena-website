from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us_view, name='contact_us'),
    path('programs/', views.programs_view, name='programs'),
    path('partner/<slug:slug>/', views.partner_request_view, name='partner_request'),
    path('thank-you/', views.thank_you, name='thank_you'), 
    path('thank/', views.thank, name='thank'), 
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<str:category>/', views.blog_view, name='blog_by_category'),
]