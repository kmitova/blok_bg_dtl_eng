# Generated by Django 4.1.3 on 2022-12-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_reply_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['publication_date'], 'verbose_name_plural': 'Replies'},
        ),
    ]
