# Generated by Django 4.0.4 on 2022-04-30 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_register_city_remove_register_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileform',
            name='username',
        ),
    ]
