# Generated by Django 5.0.2 on 2024-03-02 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0009_alter_inventorymaster_created_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 2, 21, 38, 43, 445081), null=True),
        ),
        migrations.AlterField(
            model_name='salesmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 2, 21, 38, 43, 445081), null=True),
        ),
    ]