# Generated by Django 3.2.7 on 2023-01-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jimyou', '0002_profilet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilet',
            name='text',
            field=models.CharField(blank=True, max_length=150, verbose_name='目標の説明'),
        ),
    ]