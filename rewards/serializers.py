from rest_framework import serializers
from .models import CustomUser, App, Task, Category, SubCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_picture', 'points']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']


class AppSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()

    class Meta:
        model = App
        fields = ['id', 'name', 'link', 'category', 'subcategory', 'points']


class TaskSerializer(serializers.ModelSerializer):
    app = AppSerializer()

    class Meta:
        model = Task
        fields = ['id', 'app', 'screenshot', 'status']
