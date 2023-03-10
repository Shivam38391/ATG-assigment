# Generated by Django 4.1.6 on 2023-02-14 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("muti_user", "0004_alter_customuser_line_alter_customuser_pincode"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="blog_images/")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Mental Health", "Mental Health"),
                            ("Heart Disease", "Heart Disease"),
                            ("Covid19", "Covid19"),
                            ("Immunization", "Immunization"),
                        ],
                        max_length=50,
                    ),
                ),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("is_draft", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
