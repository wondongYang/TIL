from django.db import models

# Create your models here.
class Articles(models.Model):
    # id
    # id = models.AutoField(primary_key=True) 1, 2, 3, 4

    title = models.CharField(max_length=10) # max_length가 필수
    content = models.TextField() # max_length 옵션
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    