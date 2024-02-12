# Generated by Django 5.0.1 on 2024-02-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0013_blogentry_comment_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='fullname',
            field=models.CharField(default='Anonimo', max_length=100),
        ),
    ]
