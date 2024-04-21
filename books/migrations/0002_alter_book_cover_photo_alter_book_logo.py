# Generated by Django 5.0.4 on 2024-04-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(upload_to='book_covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='logo',
            field=models.ImageField(upload_to='book_logos/'),
        ),
    ]
