# Generated by Django 4.0.1 on 2022-01-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('아우터', '아우터'), ('트레이닝', '트레이닝'), ('스커트', '스커트'), ('가방', '가방'), ('패션소품', '패션소품'), ('언더웨어', '언더웨어'), ('기타', '기타'), ('신발', '신발'), ('상의', '상의'), ('원피스/세트', '원피스/세트'), ('주얼리', '주얼리'), ('팬츠', '팬츠')], default='아우터', max_length=80),
        ),
    ]
