from django.contrib import admin
from .models import (
    SiteTextContent, TeamMember, Service, Project, ProjectCategory,
    Game, FAQ, Testimonial, ClientLogo, ContactMessage
)


# @admin.register(SiteTextContent)
class SiteTextContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value_ar', 'value_en', 'note')
    search_fields = ('key', 'value_ar', 'value_en')
    list_per_page = 20


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'role_ar')
    search_fields = ('name_ar', 'name_en', 'role_ar', 'role_en')
    list_per_page = 20


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'title_en', 'icon')
    search_fields = ('title_ar', 'title_en')
    list_per_page = 20


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'get_categories', 'date')
    list_filter = ('categories', 'date')
    search_fields = ('title_ar', 'title_en', 'description_ar', 'description_en')
    list_per_page = 20
    
    def get_categories(self, obj):
        return ", ".join([cat.name_ar for cat in obj.categories.all()])
    get_categories.short_description = 'التصنيفات'


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en')


@admin.register(Game)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en', 'url')
    search_fields = ('name_ar', 'name_en')
    list_per_page = 20


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question_ar', 'question_en')
    search_fields = ('question_ar', 'question_en', 'answer_ar', 'answer_en')
    list_per_page = 20


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    search_fields = ('name', 'content_ar', 'content_en')
    list_filter = ('rating', 'created_at')
    readonly_fields = ('created_at',)
    list_per_page = 20


@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en')
    search_fields = ('name_ar', 'name_en')
    list_per_page = 20


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'sent_at')
    search_fields = ('firstname', 'lastname', 'email', 'message')
    readonly_fields = ('sent_at',)
    list_filter = ('sent_at',)
    list_per_page = 20
