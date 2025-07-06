from django.contrib import admin
from .models import Program, PartnerRequest,ContactMessage,TeamMember,ProgramCategory
from .models import BlogPost


# Register your models here.


admin.site.register(PartnerRequest)
admin.site.register(ContactMessage)
admin.site.register(BlogPost)
admin.site.register(TeamMember)
@admin.register(ProgramCategory)
class ProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}