# Generated by Django 4.2 on 2023-05-12 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0007_payment_current_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="current_amount",
        ),
    ]
