# Generated by Django 3.0.5 on 2020-09-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200915_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemachines',
            name='model',
            field=models.CharField(choices=[('base', 'base'), ('premium', 'premium'), ('delux', 'delux')], max_length=200),
        ),
        migrations.AlterField(
            model_name='coffeemachines',
            name='product_type',
            field=models.CharField(choices=[('COFFEE_MACHINE_LARGE', 'COFFEE_MACHINE_LARGE'), ('COFFEE_MACHINE_SMALL', 'COFFEE_MACHINE_SMALL'), ('ESPRESSO_MACHINE', 'ESPRESSO_MACHINE')], max_length=70),
        ),
    ]