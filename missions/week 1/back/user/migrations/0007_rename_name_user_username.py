# Generated by Django 4.0.1 on 2022-01-07 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
