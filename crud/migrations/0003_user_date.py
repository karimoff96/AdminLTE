# Generated by Django 3.2.9 on 2021-11-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
