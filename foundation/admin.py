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


class GhanaProjectInLine(admin.TabularInline):
    model = GhanaProject
    extra = 2


class CategoryProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['image', 'title', 'content', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']
    }), ]
    inlines = [GhanaProjectInLine]


admin.site.register(GhanaCategory, CategoryProjectAdmin)


class USAProjectInLine(admin.TabularInline):
    model = USAProject
    extra = 2


class CategoryProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['image', 'title', 'content', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']
    }), ]
    inlines = [USAProjectInLine]


admin.site.register(USACategory, CategoryProjectAdmin)



class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 2


class CategoryGalleryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'image', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']
    }), ]
    inlines = [GalleryInLine]


admin.site.register(GalleryCategory, CategoryGalleryAdmin)
