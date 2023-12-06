# Generated by Django 4.2.7 on 2023-12-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0031_alter_box_options_alter_boxitem_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="consignee",
            options={
                "default_manager_name": "objects",
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "verbose_name": "Consignee",
            },
        ),
        migrations.RemoveIndex(
            model_name="consignee",
            name="edc_lab_con_name_2de87e_idx",
        ),
        migrations.AddIndex(
            model_name="consignee",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_con_modifie_970fb3_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="consignee",
            index=models.Index(
                fields=["user_modified", "user_created"], name="edc_lab_con_user_mo_a53323_idx"
            ),
        ),
    ]
