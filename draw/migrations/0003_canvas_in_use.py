# Generated by Django 3.2.7 on 2021-09-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_auto_20210910_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='in_use',
            field=models.BooleanField(null=True),
        ),
    ]
