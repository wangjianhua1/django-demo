from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    nick = models.CharField(max_length=20)
    create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
