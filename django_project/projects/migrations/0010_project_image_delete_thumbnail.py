# Generated by Django 4.2 on 2023-05-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0009_alter_project_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name="Thumbnail",
        ),
    ]