# Generated by Django 5.0.1 on 2024-01-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Applicant",
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
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("introduction", models.TextField()),
                ("motivation", models.TextField()),
                (
                    "activity_attachment",
                    models.FileField(upload_to="activity_attachments/"),
                ),
                ("github_or_tistory", models.URLField(blank=True)),
            ],
        ),
    ]
