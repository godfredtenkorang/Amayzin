from django.contrib import admin
from .models import Sponsorship, YouTube, GalleryCategory, Gallery, Contact, News, VolunteerApplication

# Register your models here.

admin.site.register(Sponsorship)
admin.site.register(YouTube)
# admin.site.register(GalleryCategory)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(VolunteerApplication)
admin.site.site_header = "Amayzin Admin"
admin.site.site_title = "Amayzin Admin Area"
admin.site.index_title = "Welcome to the Amayzin Admin Area"


class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 2


class CategoryGalleryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'image', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']
    }), ]
    inlines = [GalleryInLine]


admin.site.register(GalleryCategory, CategoryGalleryAdmin)
