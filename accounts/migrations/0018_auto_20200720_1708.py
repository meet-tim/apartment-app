# Generated by Django 3.0.2 on 2020-07-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]