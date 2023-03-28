# Generated by Django 4.1 on 2022-09-09 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image_link", models.CharField(max_length=50)),
                ("question_text", models.CharField(max_length=50)),
                ("cert_text", models.CharField(max_length=50)),
                ("no_count", models.IntegerField()),
                ("yes_count", models.IntegerField()),
                ("count", models.IntegerField()),
                ("not_sure_count", models.IntegerField()),
                (
                    "final_answer",
                    models.IntegerField(choices=[(0, "No"), (1, "Yes"), (-1, "Not Answered")], default=-1),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question_User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("answer", models.IntegerField()),
                (
                    "question",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="image_caption.question"),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
