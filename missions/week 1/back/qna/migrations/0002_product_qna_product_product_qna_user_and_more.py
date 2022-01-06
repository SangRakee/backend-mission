# Generated by Django 4.0.1 on 2022-01-06 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0003_alter_product_cart'),
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_qna',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products_feature', to='product.product'),
        ),
        migrations.AddField(
            model_name='product_qna',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users_feature', to='user.user'),
        ),
        migrations.AlterField(
            model_name='product_qna',
            name='datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='작성일'),
        ),
    ]
