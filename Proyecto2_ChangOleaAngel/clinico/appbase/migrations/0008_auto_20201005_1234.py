# Generated by Django 3.1.2 on 2020-10-05 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0007_auto_20201005_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='hora',
            field=models.TimeField(default=datetime.time(12, 34, 46, 152158), verbose_name='Hora'),
        ),
    ]
