# Generated by Django 3.1.2 on 2021-01-23 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20210116_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['id']},
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('name', 'short_name')},
        ),
    ]
