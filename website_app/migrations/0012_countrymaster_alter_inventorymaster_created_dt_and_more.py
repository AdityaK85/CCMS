# Generated by Django 5.0.2 on 2024-03-02 16:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0011_rename_customer_addr_salesmaster_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 2, 21, 54, 4, 705239), null=True),
        ),
        migrations.AlterField(
            model_name='salesmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 2, 21, 54, 4, 705239), null=True),
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website_app.countrymaster')),
            ],
        ),
    ]