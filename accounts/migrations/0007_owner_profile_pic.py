# Generated by Django 3.0.2 on 2020-07-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_owner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
