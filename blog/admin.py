from django.contrib import admin
from .models import Blog, Category
from django.utils.translation import gettext_lazy as site


admin.site.site_header = site("Portal Yönetimi")
admin.site.site_title = site("Portal Yönetimi")
# admin.site.index_title = site("Portal Yönetimine Hoşgeldiniz")

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "slug", "image",)
    list_editable = ("is_active", "is_home",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)
    list_filter = ("category","is_active", "is_home",)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    readonly_fields = ("slug",)
    search_fields = ("name", "slug",)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category, CategoryAdmin)