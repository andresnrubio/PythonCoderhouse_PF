# Generated by Django 5.0.1 on 2024-01-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=400)),
                ('date', models.DateField()),
            ],
        ),
    ]