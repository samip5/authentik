# Generated by Django 4.1.4 on 2022-12-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_policies", "0008_policybinding_authentik_p_policy__534e15_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="policy",
            name="name",
            field=models.TextField(default="unnamed-policy"),
            preserve_default=False,
        ),
    ]
