# Generated by Django 5.1.1 on 2024-10-08 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.TextField()),
                ('product_manufacture_year', models.PositiveIntegerField(blank=True)),
                ('product_base_price', models.FloatField()),
                ('product_verify', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_imagess', to='seller.productinformation')),
            ],
        ),
    ]
