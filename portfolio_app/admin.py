from django.contrib import admin
from .models import AboutMe, BlogPost, Certificate, Skill, Project, ContactMessage

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'kicker', 'quote')
    fieldsets = (
        ('Header & Media Upload', {
            'fields': ('kicker', 'title', 'image_file', 'image')
        }),
        ('Biography Paragraphs', {
            'fields': ('paragraph_1', 'paragraph_2', 'paragraph_3', 'paragraph_4')
        }),
        ('Highlight Quote', {
            'fields': ('quote',)
        }),
    )

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'date_display', 'read_time', 'is_published', 'created_at')
    list_filter = ('tag', 'is_published', 'created_at')
    search_fields = ('title', 'summary', 'tag')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'tag', 'date_display', 'read_time', 'summary', 'image_file', 'featured_image', 'is_published')
        }),
        ('Content JSON', {
            'classes': ('collapse',),
            'fields': ('content_json',),
            'description': "JSON structure containing array or dictionary of article content uploaded by admin."
        }),
    )

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image_file', 'image', 'order')
    list_editable = ('order',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_file', 'image', 'accent', 'order')
    list_editable = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image_file', 'image', 'link')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
