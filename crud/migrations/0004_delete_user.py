# Generated by Django 3.2.9 on 2021-11-13 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_user_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]