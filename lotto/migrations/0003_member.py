# Generated by Django 2.1.2 on 2018-10-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
