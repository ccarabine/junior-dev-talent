# Generated by Django 3.2 on 2022-03-30 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220328_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category'], 'verbose_name_plural': 'Products'},
        ),
    ]