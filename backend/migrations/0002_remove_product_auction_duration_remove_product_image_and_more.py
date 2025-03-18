# Generated by Django 5.1.4 on 2025-03-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='auction_duration',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='auction_duration_hours',
            field=models.IntegerField(default=24),
        ),
    ]
