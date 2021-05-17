# Generated by Django 3.2 on 2021-05-17 03:15

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_twitter_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]