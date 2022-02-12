from django.db import models
from market.models import Market
from cart.models import Cart
from user.models import User


# Product 테이블
class Product(models.Model):


    category_choices={
        ('아우터', "아우터"),
        ('상의', "상의"),
        ('원피스/세트', "원피스/세트"),
        ('팬츠', "팬츠"),
        ('스커트', "스커트"),
        ('트레이닝', "트레이닝"),
        ('가방', "가방"),
        ('신발', "신발"),
        ('패션소품', "패션소품"),
        ('주얼리', "주얼리"),
        ('언더웨어', "언더웨어"),
        ('기타', "기타"),
    }

    id = models.AutoField(primary_key=True) # product_id
    category = models.CharField(max_length=80,choices=category_choices, default="아우터")  # 카테고리
    name = models.CharField(max_length=128, verbose_name='제품명') # 제품명
    price = models.IntegerField(verbose_name='가격', default=0) # 가격
    sale_price = models.IntegerField(verbose_name="할인 가격", default=0) # 할인 가격
    description = models.TextField(max_length=255, verbose_name='제품설명') # 제품설명
    image = models.ImageField(upload_to='', null=True, verbose_name='제품 이미지')  # 이미지
    image_detail = models.ImageField(upload_to='', null=True, verbose_name='제품 상세이미지')  # 상세 이미지
    is_deleted = models.BooleanField(default=False) # 삭제여부
    is_hidden = models.BooleanField(default=False, verbose_name="히든 상품") # 숨긴여부
    is_sold_out = models.BooleanField(default=False, verbose_name="품절 상품") # 품절여부
    hit_count = models.IntegerField(verbose_name='조회수', default=0) # 조회수
    like_count = models.IntegerField(verbose_name='좋아요수', default=0)  # 좋아요수
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='업데이트일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='갱신일')  # 갱신날짜

    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='product')  # market_id


# Product_options 테이블
class Product_option(models.Model):
    id = models.AutoField(primary_key=True)  # Product_option_id
    reg_date = models.DateTimeField(auto_now=True, verbose_name='등록일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='등록일')  # 갱신날짜
    opt1_type = models.CharField(max_length=128, verbose_name='옵션1 유형') # 옵션1 유형
    opt1_name = models.CharField(max_length=128, verbose_name='옵션1 이름')  # 옵션1 이름
    opt1_price = models.IntegerField(verbose_name='옵션1 추가가격', default=0)  # 옵션1 추가가격
    opt1_stock = models.IntegerField(verbose_name='옵션1 재고수량')  # 옵션1 재고수량
    opt2_type = models.CharField(max_length=128, null=True ,verbose_name='옵션2 유형', default=None) # 옵션2 유형
    opt2_name = models.CharField(max_length=128, null=True ,verbose_name='옵션2 유형', default=None)  # 옵션2 이름
    opt2_price = models.IntegerField(null=True ,verbose_name='옵션2 추가가격', default=None)  # 옵션2 추가가격
    opt2_stock = models.IntegerField(null=True ,verbose_name='옵션2 재고수량', default=None)  # 옵션2 재고수량
    # opt3_type = models.CharField(max_length=128, null=True ,verbose_name='옵션3 유형', default=None) # 옵션3 유형
    # opt3_name = models.CharField(max_length=128, null=True ,verbose_name='옵션3 유형', default=None)  # 옵션3 이름
    # opt3_price = models.IntegerField(null=True ,verbose_name='옵션3 추가가격', default=None)  # 옵션3 추가가격
    # opt3_stock = models.IntegerField(null=True ,verbose_name='옵션3 재고수량', default=None)  # 옵션1 재고수량

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_options')  # product_id


# Product_qna 테이블
class Product_qna(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=128, verbose_name='질문제목', default="")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='갱신날짜')  # 갱신날짜
    content = models.TextField(max_length=255, verbose_name='질문내용')
    # datetime = models.DateTimeField(auto_now=True, verbose_name='작성일')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_feature',default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_feature',default="")