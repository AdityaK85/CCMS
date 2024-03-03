# Generated by Django 5.0.2 on 2024-03-03 06:25

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0018_purchasedmaster_created_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 11, 55, 15, 218444), null=True),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='supplier_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website_app.purchasedmaster'),
        ),
        migrations.AlterField(
            model_name='purchasedmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 11, 55, 15, 218444), null=True),
        ),
        migrations.AlterField(
            model_name='salesmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 11, 55, 15, 218444), null=True),
        ),
    ]
