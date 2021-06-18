from django.db import models

class Post(models.Model):
    title = models.CharField(
        'Title', max_length=100,
    )
    body = models.TextField(
        'Contents'
    )
    created_at = models.DateField(
        'Created date', auto_now_add=True,
    )
