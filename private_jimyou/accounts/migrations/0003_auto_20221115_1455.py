# Generated by Django 3.2.7 on 2022-11-15 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='USER',
        ),
        migrations.DeleteModel(
            name='USERDATA',
        ),
    ]
