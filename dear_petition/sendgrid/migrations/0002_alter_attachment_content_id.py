# Generated by Django 3.2.13 on 2022-10-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sendgrid", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="content_id",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="Content ID"
            ),
        ),
    ]
