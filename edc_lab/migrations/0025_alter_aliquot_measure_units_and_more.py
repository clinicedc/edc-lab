# Generated by Django 4.1.7 on 2023-03-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0024_alter_manifestitem_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aliquot",
            name="measure_units",
            field=models.CharField(
                choices=[
                    ("mL", "mL"),
                    ("uL", "uL"),
                    ("spots", "spots"),
                    ("n/a", "Not applicable"),
                ],
                default="mL",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaliquot",
            name="measure_units",
            field=models.CharField(
                choices=[
                    ("mL", "mL"),
                    ("uL", "uL"),
                    ("spots", "spots"),
                    ("n/a", "Not applicable"),
                ],
                default="mL",
                max_length=25,
            ),
        ),
    ]
