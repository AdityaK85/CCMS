# Generated by Django 5.0.2 on 2024-03-03 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0021_alter_inventorymaster_created_dt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='inventorymaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 17, 39, 5, 49244), null=True),
        ),
        migrations.AlterField(
            model_name='purchasedmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 17, 39, 5, 49244), null=True),
        ),
        migrations.AlterField(
            model_name='salesmaster',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 3, 17, 39, 5, 49244), null=True),
        ),
    ]