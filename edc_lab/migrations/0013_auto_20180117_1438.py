# Generated by Django 2.0.1 on 2018-01-17 12:38

import django.db.models.deletion
import edc_sites.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("edc_lab", "0012_auto_20180114_1438"),
    ]

    operations = [
        migrations.AlterModelOptions(name="order", options={}),
        migrations.AlterModelManagers(
            name="aliquot",
            managers=[("on_site", edc_sites.models.CurrentSiteManager())],
        ),
        migrations.AlterModelManagers(
            name="box", managers=[("on_site", edc_sites.models.CurrentSiteManager())]
        ),
        migrations.AlterModelManagers(
            name="manifest",
            managers=[("on_site", edc_sites.models.CurrentSiteManager())],
        ),
        migrations.AlterModelManagers(
            name="order", managers=[("on_site", edc_sites.models.CurrentSiteManager())]
        ),
        migrations.AlterModelManagers(
            name="result", managers=[("on_site", edc_sites.models.CurrentSiteManager())]
        ),
        migrations.AlterModelManagers(
            name="resultitem",
            managers=[("on_site", edc_sites.models.CurrentSiteManager())],
        ),
        migrations.AddField(
            model_name="aliquot",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="box",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="historicalaliquot",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="historicalbox",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="historicalmanifest",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="historicalorder",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="historicalresult",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="historicalresultitem",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="manifest",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="result",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
        migrations.AddField(
            model_name="resultitem",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
    ]
