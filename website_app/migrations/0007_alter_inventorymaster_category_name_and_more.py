# Generated by Django 5.0.2 on 2024-03-02 14:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0006_alter_inventorymaster_created_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymaster',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_app.categorymaster'),
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 2, 20, 2, 18, 548606), null=True),
        ),
        migrations.AlterField(
            model_name='salesmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 2, 20, 2, 18, 548606), null=True),
        ),
    ]
