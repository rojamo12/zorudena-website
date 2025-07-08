from django.contrib import admin
from .models import Blog, Program, PartnerRequest, ContactMessage, TeamMember, ProgramCategory, BlogPost

# Register models without special admin classes
admin.site.register(Blog)
admin.site.register(PartnerRequest)
admin.site.register(ContactMessage)
admin.site.register(BlogPost)
admin.site.register(TeamMember)

# Register ProgramCategory with a custom admin class
@admin.register(ProgramCategory)
class ProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register Program with a custom admin class
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}

