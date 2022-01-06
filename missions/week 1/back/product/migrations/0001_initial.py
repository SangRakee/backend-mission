# Generated by Django 4.0.1 on 2022-01-06 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0002_remove_cart_id_alter_cart_user'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='제품명')),
                ('count', models.IntegerField(verbose_name='재고')),
                ('description', models.CharField(max_length=255, verbose_name='제품설명')),
                ('register', models.DateTimeField(auto_now=True, verbose_name='등록일')),
                ('size', models.CharField(max_length=128, verbose_name='사이즈')),
                ('cart', models.ManyToManyField(blank=True, related_name='cart', to='cart.Cart')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='seller.seller')),
            ],
        ),
    ]
