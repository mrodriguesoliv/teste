# Generated by Django 5.0.6 on 2024-05-13 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_delete_page"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="text",
            new_name="body",
        ),
    ]