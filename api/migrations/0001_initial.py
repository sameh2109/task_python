# Generated by Django 3.0.5 on 2020-09-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeMachines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(default='', max_length=70)),
                ('code', models.CharField(default='', max_length=200)),
                ('water_line_compatible', models.BooleanField(default=False)),
            ],
        ),
    ]
