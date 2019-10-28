# Generated by Django 2.2.5 on 2019-10-27 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('laptops', 'Laptops'), ('stationery', 'Stationery'), ('phones', 'Phones'), ('IDs', 'IDs'), ('Wallet & Purses', 'Wallet & Purses'), ('other', 'Other')], default='other', max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('When', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='item_images')),
                ('claimed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('date_of_loss', models.DateField(default=django.utils.timezone.now)),
                ('date_claimed', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('image', models.ImageField(blank=True, default='default.png', help_text='OPTIONAL! Upload any image of the item as proof of ownership!', null=True, upload_to='claims_images')),
                ('accepted', models.BooleanField(null=True)),
                ('claimed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_claimed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Post')),
            ],
        ),
    ]