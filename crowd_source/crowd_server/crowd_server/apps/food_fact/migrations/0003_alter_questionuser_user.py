# Generated by Django 4.1 on 2022-09-09 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("food_fact", "0002_alter_question_count_alter_question_no_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionuser",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="qu_food_fact", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]