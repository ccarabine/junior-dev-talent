# Generated by Django 3.2 on 2022-04-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220401_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]