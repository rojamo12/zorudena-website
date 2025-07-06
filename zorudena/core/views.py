from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import strip_tags
from django.utils.text import Truncator
from .models import Program, BlogPost,TeamMember,ProgramCategory
from .forms import PartnerRequestForm, ContactMessageForm


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact_us_view(request):  # Renamed to avoid conflict
    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Send email notification
            send_mail(
                subject='New Contact Message',
                message=f"""
New contact message received:

Name: {contact_message.name}
Email: {contact_message.email}
Message: {contact_message.message}
""",
                from_email='omirambe223@gmail.com',
                recipient_list=['omirambe223@gmail.com'],
                fail_silently=False,
            )
            return redirect('thank')
    return render(request, 'contact_us.html', {'form': form})

def programs_view(request):
    categories = ProgramCategory.objects.prefetch_related('programs').all()
    return render(request, 'programs.html', {'categories': categories})

def partner_request_view(request, slug):
    program = get_object_or_404(Program, slug=slug)
    return render(request, 'partner_request.html', {'program': program})


def partner_form(request):
    return render(request, 'partner_form.html')


def thank_you(request):
    return render(request, 'thank_you.html')


def thank(request):
    return render(request, 'thank.html')


def partner_request_view(request, slug):
    program = get_object_or_404(Program, slug=slug)
    if request.method == 'POST':
        form = PartnerRequestForm(request.POST)
        if form.is_valid():
            partner_request = form.save(commit=False)
            partner_request.program = program
            partner_request.save()

            # Send email to admin
            send_mail(
                subject=f"New Partnership Request for {program.title}",
                message=f"""
You have received a new partnership request:

Name: {partner_request.name}
Email: {partner_request.email}
Phone: {partner_request.phone}
Message: {partner_request.message}
Program: {program.title}
""",
                from_email='omirambe223@gmail.com',
                recipient_list=['omirambe223@gmail.com'],
                fail_silently=False,
            )
            return redirect('thank_you')
    else:
        form = PartnerRequestForm()

    return render(request, 'partner_form.html', {'form': form, 'program': program})


def blog_view(request, category=None):
    posts = BlogPost.objects.all().order_by('-date_posted')
    if category:
        posts = posts.filter(category=category)

    for post in posts:
        post.short_content = Truncator(strip_tags(post.content)).chars(150, truncate=' ...')

    return render(request, 'blog.html', {'posts': posts, 'current_category': category})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})


def team_view(request):
    categories = ['leadership', 'programs', 'finance', 'volunteers', 'advisory']
    team_data = {cat: TeamMember.objects.filter(category=cat) for cat in categories}
    return render(request, 'team.html', {'team_data': team_data})
