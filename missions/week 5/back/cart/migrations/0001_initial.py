# Generated by Django 3.2 on 2022-02-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20220209_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
            ],
        ),
    ]