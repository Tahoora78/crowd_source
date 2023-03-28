from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sentiment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionuser",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="qu_sentiment", to="sentiment.question"
            ),
        ),
    ]
