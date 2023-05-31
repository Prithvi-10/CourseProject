from django.urls import path
from displayapp import views

urlpatterns=[
    path('homepage/',views.homepage, name="homepage"),
    path('productpage/<catg>',views.productpage,name="productpage"),
    path('detailspage/<int:dataid>/', views.detailspage, name="detailspage"),
    path('signin/', views.signin, name="signin"),
    path('user_reg/', views.user_reg, name="user_reg"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),
    path('savecart/', views.savecart, name="savecart"),
    path('displaycartdata/', views.displaycartdata, name="displaycartdata"),

]