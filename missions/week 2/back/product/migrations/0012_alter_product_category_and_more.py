# Generated by Django 4.0.1 on 2022-01-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('가방', '가방'), ('아우터', '아우터'), ('팬츠', '팬츠'), ('트레이닝', '트레이닝'), ('패션소품', '패션소품'), ('언더웨어', '언더웨어'), ('기타', '기타'), ('스커트', '스커트'), ('원피스/세트', '원피스/세트'), ('주얼리', '주얼리'), ('신발', '신발'), ('상의', '상의')], default='아우터', max_length=80),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt2_name',
            field=models.CharField(max_length=128, null=True, verbose_name='옵션2 유형'),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt2_price',
            field=models.IntegerField(default=0, null=True, verbose_name='옵션2 추가가격'),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt2_stock',
            field=models.IntegerField(null=True, verbose_name='옵션2 재고수량'),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt3_name',
            field=models.CharField(max_length=128, null=True, verbose_name='옵션3 유형'),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt3_price',
            field=models.IntegerField(default=0, verbose_name='null=True ,옵션3 추가가격'),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt3_stock',
            field=models.IntegerField(verbose_name='null=True ,옵션3 재고수량'),
        ),
        migrations.AlterField(
            model_name='product_options',
            name='opt3_type',
            field=models.CharField(max_length=128, null=True, verbose_name='옵션3 유형'),
        ),
    ]
