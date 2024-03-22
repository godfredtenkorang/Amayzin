from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *

# Register your models here.


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Sponsorship)
admin.site.register(YouTube, AdminVideo)
# admin.site.register(GalleryCategory)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(VolunteerApplication)
admin.site.site_header = "Amayzin Admin"
admin.site.site_title = "Amayzin Admin Area"
admin.site.index_title = "Welcome to the Amayzin Admin Area"


class ProjectInLine(admin.TabularInline):
    model = Project
    extra = 2


class CategoryProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'content', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']
    }), ]
    inlines = [ProjectInLine]


admin.site.register(ProjectCategory, CategoryProjectAdmin)


class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 2


class CategoryGalleryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'image', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']
    }), ]
    inlines = [GalleryInLine]


admin.site.register(GalleryCategory, CategoryGalleryAdmin)
