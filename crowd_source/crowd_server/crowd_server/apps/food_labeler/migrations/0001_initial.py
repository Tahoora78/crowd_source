# Generated by Django 4.1 on 2022-09-08 19:22

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
                ("question_text", models.CharField(max_length=200)),
                ("image_link", models.URLField(blank=True, null=True)),
                ("no_count", models.PositiveIntegerField(default=0)),
                ("yes_count", models.PositiveIntegerField(default=0)),
                ("total_count", models.PositiveIntegerField(default=0)),
                ("not_sure_count", models.PositiveIntegerField(default=0)),
                (
                    "final_answer",
                    models.IntegerField(choices=[(0, "No"), (1, "Yes"), (-1, "Not Answered")], default=-1),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "answer",
                    models.IntegerField(
                        choices=[(0, "No"), (1, "Yes"), (2, "Not Sure"), (-1, "Not Answered")], default=-1
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="food_labeler.question"),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
