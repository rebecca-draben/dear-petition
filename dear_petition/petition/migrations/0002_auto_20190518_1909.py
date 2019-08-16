# Generated by Django 2.2 on 2019-05-18 19:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("petition", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="ciprsrecord",
            name="data",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ciprsrecord",
            name="report_pdf",
            field=models.FileField(upload_to="ciprs/", verbose_name="Report PDF"),
        ),
    ]
