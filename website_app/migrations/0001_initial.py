# Generated by Django 5.0.2 on 2024-03-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_no', models.CharField(blank=True, max_length=200, null=True)),
                ('category_name', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('unit_price', models.CharField(blank=True, max_length=200, null=True)),
                ('supplier_info', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]