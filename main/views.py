
from django.shortcuts import render
from .models import Blog  # Make sure you have a Blog model
from .models import Program



def home(request):
    return render(request, 'main/home.html')

def about_us(request):
    return render(request, 'main/about.html')  # make sure this template exists



def programs(request):
    all_programs = Program.objects.all()
    return render(request, 'main/programs.html', {'programs': all_programs})


def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    return render(request, 'main/contact.html')   


def blog_by_category(request, category):
    posts = Blog.objects.filter(category__iexact=category)
    return render(request, 'main/blog_by_category.html', {'posts': posts, 'category': category})
