# Generated by Django 4.0.1 on 2022-01-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_alter_product_qna_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_qna',
            name='title',
            field=models.CharField(default='', max_length=128, verbose_name='질문제목'),
        ),
    ]
