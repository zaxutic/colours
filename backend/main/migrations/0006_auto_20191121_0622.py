# Generated by Django 2.2.4 on 2019-11-21 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_is_stuff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
