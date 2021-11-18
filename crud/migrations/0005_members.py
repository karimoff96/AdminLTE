# Generated by Django 3.2.9 on 2021-11-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]