from django.db import models

# Create your models here.
class Nikki(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=20)
    content = models.CharField(verbose_name="本文", max_length=100)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

    def __str__(self):
        return self.title