# https://zenn.dev/shimakaze_soft/articles/7f3a12881614b5
from django.db import models
from accounts.models import CustomUser


class Profile(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    gender = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    favorite_words = models.CharField(max_length=50, blank=True)
    # class Meta:
    #     verbose_name_plural = 'Profile'
    # def __str__(self):
    #     return self.gender

# https://di-acc2.com/programming/python/1694/