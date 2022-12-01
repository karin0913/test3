# Generated by Django 3.2.7 on 2022-12-01 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiletest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.DateField(blank=True, null=True, verbose_name='目標達成日')),
                ('title', models.CharField(blank=True, max_length=30, verbose_name='目標の名前')),
                ('text', models.CharField(blank=True, max_length=50, verbose_name='目標の説明')),
                ('text1', models.CharField(blank=True, max_length=50, verbose_name='目標の説明')),
                ('text2', models.CharField(blank=True, max_length=50, verbose_name='目標の説明')),
                ('text3', models.CharField(blank=True, max_length=50, verbose_name='目標の説明')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
