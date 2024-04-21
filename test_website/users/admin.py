from django.contrib import admin

from users.models import User


class QualifyExecutorsFilter(admin.SimpleListFilter):
    title = 'Квалификация исполнителей'
    parameter_name = 'qualify'

    def lookups(self, request, model_admin):
        return [
            ('Нет опыта', 'Нет опыта'),
            ('Несколько месяцев', 'Несколько месяцев'),
            ('От 1 до 3 лет', 'От 1 до 3 лет'),
            ('От 3 до 5 лет', 'От 3 до 5 лет'),
            ('Более 5 лет', 'Более 5 лет')
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(experience=self.value())
        return queryset


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name', 'username', 'email', 'password',
              'is_customer', 'about', 'experience', 'telegram',
              'last_login', 'date_joined', 'is_staff']
    list_display = ('last_name', 'first_name', 'email', 'telegram', 'is_customer')
    ordering = ('last_name', 'first_name')
    list_per_page = 10
    search_fields = ('last_name__startswith', 'first_name__startswith')
    list_filter = (QualifyExecutorsFilter, )