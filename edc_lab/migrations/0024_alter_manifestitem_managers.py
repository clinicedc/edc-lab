# Generated by Django 3.2.13 on 2022-09-29 14:42

from django.db import migrations
import django.db.models.manager
import edc_sites.models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0023_auto_20220704_1841"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="manifestitem",
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
    ]
