from django.db import models

# Create your models here.
class Topic(model,Model):
    """用户学习的主题"""

    text=models.CharField(max_length=200)
    date_added = model.DateTimeField(auto_now_add=True)