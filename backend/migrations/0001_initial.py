# Generated by Django 5.1.4 on 2025-03-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/images')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bid_start_date', models.DateTimeField(auto_now_add=True)),
                ('auction_duration', models.DurationField()),
            ],
        ),
    ]
