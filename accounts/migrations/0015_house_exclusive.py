# Generated by Django 3.0.2 on 2020-07-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200713_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='exclusive',
            field=models.BooleanField(default=False),
        ),
    ]
