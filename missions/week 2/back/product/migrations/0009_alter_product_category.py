# Generated by Django 4.0.1 on 2022-01-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_register_product_reg_date_remove_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('원피스/세트', '원피스/세트'), ('상의', '상의'), ('팬츠', '팬츠'), ('가방', '가방'), ('스커트', '스커트'), ('패션소품', '패션소품'), ('언더웨어', '언더웨어'), ('기타', '기타'), ('주얼리', '주얼리'), ('신발', '신발'), ('트레이닝', '트레이닝'), ('아우터', '아우터')], default='아우터', max_length=80),
        ),
    ]
