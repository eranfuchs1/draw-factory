# Generated by Django 3.2.7 on 2021-10-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0003_canvas_in_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='in_use_ts',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
