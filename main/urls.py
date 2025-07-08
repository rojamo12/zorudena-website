from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
     #path('contact/', views.contact_us_view, name='contact_us'),
    path('contact/', views.contact, name='contact'),  # <-- this must exist
    
    path('programs/', views.programs_view, name='programs'),
    path('partner/<slug:slug>/', views.partner_request_view, name='partner_request'),
    
    path('thank-you/', views.thank_you, name='thank_you'),
    path('thank/', views.thank, name='thank'),
    
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<str:category>/', views.blog_view, name='blog_by_category'),

    path('team/', views.team_view, name='team'),
]


 #from django.urls import path  # ✅ include is now imported
 #from . import views

 #urlpatterns = [
    # path('', views.home, name='home'),                           # Homepage
     #path('contact/', views.contact, name='contact'),       # Contact page
    # path('about/', views.about_us, name='about_us'),             # About page
    # path('blog/', views.blog, name='blog'),                         # Include blog app's URLs
    # path('programs/', views.programs, name='programs'),          # Programs page
    # path('blog/category/<str:category>/', views.blog_by_category, name='blog_by_category'),  # Blog category filter
 #]


 #from django.urls import path
 #from . import views

 #urlpatterns = [
   #  path('', views.home, name='home'),
     #path('about/', views.about_us, name='about_us'),
     #path('contact/', views.contact_us_view, name='contact_us'),
    # path('programs/', views.programs_view, name='programs'),
     #path('partner/<slug:slug>/', views.partner_request_view, name='partner_request'),
    # path('thank-you/', views.thank_you, name='thank_you'),
     #path('thank/', views.thank, name='thank'),
     #path('blog/', views.blog_view, name='blog'),
     #path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
     #path('blog/category/<str:category>/', views.blog_view, name='blog_by_category'),
     #path('team/', views.team_view, name='team'),
 #]

