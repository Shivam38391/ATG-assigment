# Generated by Django 4.1.6 on 2023-02-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("muti_user", "0002_customuser_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(blank=True, max_length=100, unique=True),
        ),
    ]
