# Generated by Django 4.2 on 2023-05-05 19:27

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_customuser_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="birth_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="country",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, null=True
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
