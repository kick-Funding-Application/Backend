# Generated by Django 4.2 on 2023-05-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_customuser_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_image",
            field=models.ImageField(blank=True, null=True, upload_to="static/images"),
        ),
    ]