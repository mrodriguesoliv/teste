# Generated by Django 5.0.6 on 2024-05-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_rename_text_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="cover",
            field=models.ImageField(default="DEFAULT VALUE", upload_to="uploads/"),
        ),
    ]
