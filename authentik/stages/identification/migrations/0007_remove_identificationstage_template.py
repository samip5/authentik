# Generated by Django 3.1.6 on 2021-02-20 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentik_stages_identification",
            "0006_identificationstage_show_matched_user",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="identificationstage",
            name="template",
        ),
    ]
