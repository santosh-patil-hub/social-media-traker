from django.contrib import admin
from .models import CustomUser, App, Task, Category, SubCategory

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'points')


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'category', 'subcategory', 'points')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'app', 'status')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
