# Generated by Django 5.0.1 on 2024-02-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.CharField(max_length=120)),
                ('introduction', models.CharField(max_length=5000)),
                ('content_list', models.JSONField(default=list)),
                ('resume', models.CharField(max_length=5000)),
                ('author', models.CharField(default='Anonimo', max_length=120)),
                ('imgUrl', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='blogEntry',
        ),
    ]
