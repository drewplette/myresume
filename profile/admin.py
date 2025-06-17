from django.contrib import admin

# Register your models here.

from .models import Resume, Contact, Portfolio, Blog, Comment
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'blog__title')
    list_filter = ('created_at',)

# This code registers the models with the Django admin site, allowing for easy management of the data through the admin interface.