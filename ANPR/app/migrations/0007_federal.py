# Generated by Django 2.2.5 on 2020-01-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200113_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='federal',
            fields=[
                ('veh_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]