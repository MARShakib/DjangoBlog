# Generated by Django 5.0.4 on 2024-04-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theblog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="My Blog", max_length=255),
        ),
    ]