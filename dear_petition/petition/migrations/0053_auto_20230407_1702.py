# Generated by Django 3.2.13 on 2023-04-07 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0052_auto_20230328_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offenserecord',
            name='disposition',
        ),
        migrations.RemoveField(
            model_name='offenserecord',
            name='is_visible',
        ),
    ]