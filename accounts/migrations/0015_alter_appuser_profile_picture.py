# Generated by Django 4.1.3 on 2022-11-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_appuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/blank-profile-picture.png', null=True, upload_to='images/'),
        ),
    ]
