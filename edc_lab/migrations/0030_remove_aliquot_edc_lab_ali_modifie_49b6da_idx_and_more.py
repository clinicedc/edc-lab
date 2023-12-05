# Generated by Django 4.2.7 on 2023-12-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0029_alter_aliquot_options_alter_box_options_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="aliquot",
            name="edc_lab_ali_modifie_49b6da_idx",
        ),
        migrations.RemoveIndex(
            model_name="box",
            name="edc_lab_box_modifie_af5133_idx",
        ),
        migrations.RemoveIndex(
            model_name="boxitem",
            name="edc_lab_box_modifie_6a2a97_idx",
        ),
        migrations.RemoveIndex(
            model_name="boxtype",
            name="edc_lab_box_modifie_eb0207_idx",
        ),
        migrations.RemoveIndex(
            model_name="manifest",
            name="edc_lab_man_modifie_aae866_idx",
        ),
        migrations.RemoveIndex(
            model_name="manifestitem",
            name="edc_lab_man_modifie_113dc0_idx",
        ),
        migrations.RemoveIndex(
            model_name="order",
            name="edc_lab_ord_modifie_33b427_idx",
        ),
        migrations.RemoveIndex(
            model_name="result",
            name="edc_lab_res_modifie_edced5_idx",
        ),
        migrations.RemoveIndex(
            model_name="resultitem",
            name="edc_lab_res_modifie_d7258d_idx",
        ),
        migrations.RemoveIndex(
            model_name="shipper",
            name="edc_lab_shi_modifie_822b3b_idx",
        ),
        migrations.AddIndex(
            model_name="aliquot",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_ali_modifie_d3de00_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="box",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_box_modifie_58c481_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="boxitem",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_box_modifie_2ea786_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="boxtype",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_box_modifie_0dfa0d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="manifest",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_man_modifie_771947_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="manifestitem",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_man_modifie_01a620_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_ord_modifie_8102e9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="result",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_res_modifie_798e22_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="resultitem",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_res_modifie_8457dc_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="shipper",
            index=models.Index(
                fields=["modified", "created"], name="edc_lab_shi_modifie_73bada_idx"
            ),
        ),
    ]
