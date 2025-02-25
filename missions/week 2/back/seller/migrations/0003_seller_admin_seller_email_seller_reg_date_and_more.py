# Generated by Django 4.0.1 on 2022-01-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_seller_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='admin',
            field=models.CharField(default='', max_length=128, verbose_name='대표자 이름'),
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.TextField(default='', max_length=255, verbose_name='이메일'),
        ),
        migrations.AddField(
            model_name='seller',
            name='reg_date',
            field=models.DateTimeField(auto_now=True, verbose_name='등록일'),
        ),
        migrations.AddField(
            model_name='seller',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='등록일'),
        ),
        migrations.AddField(
            model_name='seller',
            name='url',
            field=models.TextField(default='', max_length=255, verbose_name='url'),
        ),
    ]
