from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='task_screenshots/')
    status = models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING')

    def save(self, *args, **kwargs):
        if self.status == 'COMPLETED':
            self.user.points += self.app.points
            self.user.save()
        super().save(*args, **kwargs)
