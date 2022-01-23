from django.urls import path
from . import views


urlpatterns = [
    # 제품 관련
    path('', views.ProductList, name="Productlist"),
    path('<int:pk>/', views.ProductDetail, name="ProductDetail"),
    path('create/', views.ProductCreate, name="ProductCreate"),
    path('update/<int:pk>/', views.ProductUpdate, name="ProductUpdate"),
    path('delete/<int:pk>/', views.ProductDelete, name="ProductDelete"),
    path('find/<str:name>/', views.ProductFind, name="ProductFind"),

    # 옵션 관련
    path('option/', views.OptionList, name="OptionList"),
    path('option/create/', views.OptionCreate, name="OptionCreate"),
    # path('option/update/<int:pk>/', views.OptionUpdate, name="OptionUpdate"),
    # path('option/delete/<int:pk>/', views.OptionDelete, name="OptionDelete"),
]