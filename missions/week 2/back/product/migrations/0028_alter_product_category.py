# Generated by Django 4.0.1 on 2022-01-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_remove_product_cart_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('팬츠', '팬츠'), ('패션소품', '패션소품'), ('가방', '가방'), ('아우터', '아우터'), ('트레이닝', '트레이닝'), ('언더웨어', '언더웨어'), ('상의', '상의'), ('스커트', '스커트'), ('원피스/세트', '원피스/세트'), ('신발', '신발'), ('기타', '기타'), ('주얼리', '주얼리')], default='아우터', max_length=80),
        ),
    ]
