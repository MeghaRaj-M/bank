# Generated by Django 4.2.5 on 2023-10-31 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0007_district_wikipedia_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='wikipedia_url',
        ),
    ]
