# Generated by Django 4.2.7 on 2023-12-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0032_alter_consignee_options_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="panel",
            name="edc_lab_pan_lab_pro_2a0c6d_idx",
        ),
        migrations.AddIndex(
            model_name="panel",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_pan_modifie_a465ed_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="panel",
            index=models.Index(
                fields=["user_modified", "user_created"], name="edc_lab_pan_user_mo_ff00b2_idx"
            ),
        ),
    ]
