# Generated by Django 4.0.5 on 2022-07-04 07:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]