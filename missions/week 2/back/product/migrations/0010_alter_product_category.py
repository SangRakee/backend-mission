# Generated by Django 4.0.1 on 2022-01-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('스커트', '스커트'), ('팬츠', '팬츠'), ('패션소품', '패션소품'), ('신발', '신발'), ('언더웨어', '언더웨어'), ('원피스/세트', '원피스/세트'), ('아우터', '아우터'), ('주얼리', '주얼리'), ('가방', '가방'), ('기타', '기타'), ('트레이닝', '트레이닝'), ('상의', '상의')], default='아우터', max_length=80),
        ),
    ]
