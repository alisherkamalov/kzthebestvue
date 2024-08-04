# Generated by Django 5.0.7 on 2024-08-04 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('fullname', models.CharField(max_length=50)),
                ('password', models.TextField()),
                ('phone', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('token', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
