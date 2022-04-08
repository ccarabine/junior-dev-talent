# Generated by Django 3.2 on 2022-04-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_userprofile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='cvs'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_user.png', null=True, upload_to='profile_images/'),
        ),
    ]