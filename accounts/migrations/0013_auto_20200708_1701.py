# Generated by Django 3.0.2 on 2020-07-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200708_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image1',
            field=models.ImageField(blank=True, default='appartment-logo.png', null=True, upload_to='house_images'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, default='appartment-logo.png', null=True, upload_to='house_images'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image3',
            field=models.ImageField(blank=True, default='appartment-logo.png', null=True, upload_to='house_images'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image4',
            field=models.ImageField(blank=True, default='appartment-logo.png', null=True, upload_to='house_images'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image5',
            field=models.ImageField(blank=True, default='appartment-logo.png', null=True, upload_to='house_images'),
        ),
    ]
