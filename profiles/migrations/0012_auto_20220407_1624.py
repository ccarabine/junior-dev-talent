# Generated by Django 3.2 on 2022-04-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20220407_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_user.png', null=True, upload_to='profile_images/'),
        ),
    ]
