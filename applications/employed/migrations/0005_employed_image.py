# Generated by Django 3.1.2 on 2021-01-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employed', '0004_auto_20210123_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='employed',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
