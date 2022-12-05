# https://zenn.dev/shimakaze_soft/articles/7f3a12881614b5
from django.db import models
from accounts.models import Usertest


class Profiletest(models.Model):
    user = models.ForeignKey(Usertest,verbose_name='ユーザー',on_delete=models.PROTECT)
    limit = models.DateField(verbose_name='目標達成日',null=True, blank=True)
    title = models.CharField(verbose_name='目標の名前',max_length=30, blank=True)
    text = models.CharField(verbose_name='目標の説明',max_length=50, blank=True)
    text1 = models.CharField(verbose_name='目標の説明',max_length=50, blank=True)
    text2 = models.CharField(verbose_name='目標の説明',max_length=50, blank=True)
    text3 = models.CharField(verbose_name='目標の説明',max_length=50, blank=True)

    # class Meta:
    #     verbose_name_plural = 'Profile'
    # def __str__(self):
    #     return self.gender

# https://di-acc2.com/programming/python/1694/