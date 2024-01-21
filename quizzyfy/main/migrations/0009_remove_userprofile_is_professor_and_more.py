# Generated by Django 4.2 on 2023-12-01 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_alter_exam_model_end_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="is_professor",
        ),
        migrations.AlterField(
            model_name="exam_model",
            name="end_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 1, 16, 18, 34, 42085)
            ),
        ),
        migrations.AlterField(
            model_name="exam_model",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 1, 16, 18, 34, 42085)
            ),
        ),
    ]