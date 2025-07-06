from django.db import models
from django.utils.text import slugify


class ProgramCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    category = models.ForeignKey(ProgramCategory, related_name='programs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='programs/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PartnerRequest(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20) 
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.program.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Education', 'Education'),
        ('Child Protection', 'Child Protection'),
        ('Health and Nutrition', 'Health and Nutrition'),
        ('Economic Empowerment', 'Economic Empowerment'),
        ('Adolescent SRHR', 'Adolescent SRHR'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def short_content(self):
        from django.utils.html import strip_tags
        from django.utils.text import Truncator
        return Truncator(strip_tags(self.content)).chars(150, truncate=' ...')

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    CATEGORY_CHOICES = [
        ('leadership', 'Leadership'),
        ('programs', 'Programs'),
        ('finance', 'Finance & Admin'),
        ('volunteers', 'Volunteers'),
        ('advisory', 'Advisory Board'),
    ]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    quote = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='team_photos/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Donation(models.Model):
    donor_name = models.CharField(max_length=100, default="Anonymous")
    donor_email = models.EmailField(default="anon@example.com")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # transaction_reference = models.CharField(max_length=100, unique=True)
    transaction_reference = models.CharField(
    max_length=100,
    unique=True,
    default="TEMP-REF"  # Temporary default for migration
)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('successful', 'Successful'),
            ('failed', 'Failed'),
        ],
        default='pending'  # <-- This is essential
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - {self.amount} ({self.status})"




