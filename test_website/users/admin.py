from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .choices import EXPERIENCE_TYPES

User = get_user_model()


class QualifyExecutorsFilter(admin.SimpleListFilter):
    title = 'Квалификация исполнителей'
    parameter_name = 'qualify'

    def lookups(self, request, model_admin):
        return EXPERIENCE_TYPES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(experience=self.value())
        return queryset


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ('username', 'password')}),
        (("Персональная информация"), {"fields": ("last_name", "first_name")}),
        (("Даты"), {"fields": ("last_login", "date_joined")}),
        (("Контакты"), {"fields": ("email", "telegram")}),
        (("Профессиональная информация"), {"fields": ("is_customer", "about", "experience")}),
    )
    list_display = ('last_name', 'first_name', 'email', 'telegram', 'is_customer')
    ordering = ('last_name', 'first_name')
    list_per_page = 10
    search_fields = ('last_name__startswith', 'first_name__startswith')
    list_filter = (QualifyExecutorsFilter, )