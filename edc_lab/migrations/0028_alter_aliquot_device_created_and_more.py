# Generated by Django 4.2.4 on 2023-08-23 01:13

import _socket
from django.db import migrations, models
import django_audit_fields.fields.hostname_modification_field


class Migration(migrations.Migration):
    dependencies = [
        ("edc_lab", "0027_alter_aliquot_managers_alter_box_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aliquot",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="aliquot",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="aliquot",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="aliquot",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="box",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="box",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="box",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="box",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="boxitem",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="boxitem",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="boxitem",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="boxitem",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="boxtype",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="boxtype",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="boxtype",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="boxtype",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="consignee",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="consignee",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="consignee",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="consignee",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaliquot",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalaliquot",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalaliquot",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaliquot",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbox",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalbox",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalbox",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbox",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalboxitem",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalboxitem",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalboxitem",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalboxitem",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalconsignee",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalconsignee",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalconsignee",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalconsignee",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmanifest",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalorder",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalresult",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalresult",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalresult",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalresult",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalresultitem",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalresultitem",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalresultitem",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalresultitem",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="historicalshipper",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicalshipper",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicalshipper",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalshipper",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="manifest",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="manifest",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="manifest",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="manifest",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="manifestitem",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="manifestitem",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="manifestitem",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="manifestitem",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="order",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="order",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="panel",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="panel",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="panel",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="panel",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="result",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="result",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="resultitem",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="resultitem",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="resultitem",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="resultitem",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="shipper",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="shipper",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="shipper",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="shipper",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
    ]
