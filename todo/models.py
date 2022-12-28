from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.TextField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to="todo_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
