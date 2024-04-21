# Generated by Django 5.0.4 on 2024-04-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_itemdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDetails1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_details1_title', models.CharField(max_length=100)),
                ('item_details1_desc', models.CharField(max_length=250)),
                ('item_details1_images', models.ImageField(upload_to='images/')),
            ],
        ),
    ]