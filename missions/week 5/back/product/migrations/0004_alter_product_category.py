# Generated by Django 3.2 on 2022-02-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('신발', '신발'), ('스커트', '스커트'), ('주얼리', '주얼리'), ('아우터', '아우터'), ('트레이닝', '트레이닝'), ('팬츠', '팬츠'), ('가방', '가방'), ('기타', '기타'), ('패션소품', '패션소품'), ('상의', '상의'), ('원피스/세트', '원피스/세트'), ('언더웨어', '언더웨어')], default='아우터', max_length=80),
        ),
    ]