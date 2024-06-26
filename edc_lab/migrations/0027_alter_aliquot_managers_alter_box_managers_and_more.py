# Generated by Django 4.2.1 on 2023-07-07 19:32

import edc_sites.models
from django.db import migrations

import edc_lab.models.aliquot
import edc_lab.models.box
import edc_lab.models.manifest.manifest
import edc_lab.models.order
import edc_lab.models.result
import edc_lab.models.result_item


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0026_alter_aliquot_options_alter_box_options_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="aliquot",
            managers=[
                ("objects", edc_lab.models.aliquot.Manager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="box",
            managers=[
                ("objects", edc_lab.models.box.BoxManager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="manifest",
            managers=[
                ("objects", edc_lab.models.manifest.manifest.Manager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="order",
            managers=[
                ("objects", edc_lab.models.order.OrderManager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="result",
            managers=[
                ("objects", edc_lab.models.result.ResultManager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="resultitem",
            managers=[
                ("objects", edc_lab.models.result_item.ResultItemManager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
    ]
