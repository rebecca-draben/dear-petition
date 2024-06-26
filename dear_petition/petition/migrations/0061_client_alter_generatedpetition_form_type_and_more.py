# Generated by Django 4.2.9 on 2024-05-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("petition", "0060_alter_contact_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "contact_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="petition.contact",
                    ),
                ),
                ("dob", models.DateField(blank=True, null=True)),
            ],
            bases=("petition.contact",),
        ),
        migrations.AlterField(
            model_name="generatedpetition",
            name="form_type",
            field=models.CharField(
                choices=[
                    ("AOC-CR-281", "AOC-CR-281"),
                    ("AOC-CR-285", "AOC-CR-285"),
                    ("AOC-CR-287", "AOC-CR-287"),
                    ("AOC-CR-288", "AOC-CR-288"),
                    ("AOC-CR-293", "AOC-CR-293"),
                    ("AOC-CR-297", "AOC-CR-297"),
                    ("AOC-CR-298", "AOC-CR-298"),
                    ("Addendum 3B", "Addendum 3B"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="petition",
            name="agencies",
            field=models.ManyToManyField(related_name="+", to="petition.contact"),
        ),
        migrations.AlterField(
            model_name="petition",
            name="form_type",
            field=models.CharField(
                choices=[
                    ("AOC-CR-281", "AOC-CR-281"),
                    ("AOC-CR-285", "AOC-CR-285"),
                    ("AOC-CR-287", "AOC-CR-287"),
                    ("AOC-CR-288", "AOC-CR-288"),
                    ("AOC-CR-293", "AOC-CR-293"),
                    ("AOC-CR-297", "AOC-CR-297"),
                    ("AOC-CR-298", "AOC-CR-298"),
                    ("Addendum 3B", "Addendum 3B"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="petitiondocument",
            name="agencies",
            field=models.ManyToManyField(related_name="+", to="petition.contact"),
        ),
        migrations.AlterField(
            model_name="petitiondocument",
            name="form_type",
            field=models.CharField(
                choices=[
                    ("AOC-CR-281", "AOC-CR-281"),
                    ("AOC-CR-285", "AOC-CR-285"),
                    ("AOC-CR-287", "AOC-CR-287"),
                    ("AOC-CR-288", "AOC-CR-288"),
                    ("AOC-CR-293", "AOC-CR-293"),
                    ("AOC-CR-297", "AOC-CR-297"),
                    ("AOC-CR-298", "AOC-CR-298"),
                    ("Addendum 3B", "Addendum 3B"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="batch",
            name="client",
            field=models.ForeignKey(
                limit_choices_to={"category": "client"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="batches",
                to="petition.client",
            ),
        ),
    ]
