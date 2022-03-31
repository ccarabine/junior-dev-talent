# Generated by Django 3.2 on 2022-03-31 12:24

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_original_bag_order_original_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=django_countries.fields.CountryField(max_length=20),
        ),
    ]
