from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(About)
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "percentage", "order", "tooltip")
    ordering = ("order",)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "percentage", "order")
    list_filter = ("category",)
    search_fields = ("name",)
    ordering = ("category", "order")

admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Experience)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)


class ServiceBulletInline(admin.TabularInline):
    model = ServiceBullet
    extra = 1  
    fields = ('text', 'order')
    ordering = ('order',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    inlines = [ServiceBulletInline]

@admin.register(ServiceBullet)
class ServiceBulletAdmin(admin.ModelAdmin):
    list_display = ('service', 'text', 'order')
    list_filter = ('service',)
    search_fields = ('text',)
    ordering = ('service', 'order')

admin.site.register(Testimonial)
admin.site.register(SocialLink)