# Generated by Django 4.1.6 on 2023-02-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("muti_user", "0006_alter_customuser_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(blank=True, upload_to="blog_images/"),
        ),
    ]
