# Generated by Django 3.0.2 on 2020-07-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='number_of_visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'visit',
                'verbose_name_plural': 'visits',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=220, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'visitor',
                'verbose_name_plural': 'visitors',
                'ordering': ['-timestamp'],
            },
        ),
    ]