from BookApp import views
from django.urls import path

urlpatterns=[
        path('index/',views.index,name="index"),
        path('logintest/',views.logintest,name="logintest"),
        path('adminlogin/',views.adminlogin,name="adminlogin"),
        path('adminlogout/',views.adminlogout,name="adminlogout"),

        path('categoryfn/',views.categoryfn,name="categoryfn"),
        path('savedata/',views.savedata,name="savedata"),
        path('displaydata/',views.displaydata,name="displaydata"),
        path('editcategory/<int:dataid>',views.editcategory,name="editcategory"),
        path('updatecategory/<int:dataid>',views.updatecategory,name="updatecategory"),
        path('deletecategory/<int:dataid>',views.deletecategory,name="deletecategory"),

        path('productfn/', views.productfn, name="productfn"),
        path('saveproduct/', views.saveproduct, name="saveproduct"),
        path('displayproduct/', views.displayproduct, name="displayproduct"),
        path('editproduct/<int:dataid>', views.editproduct, name="editproduct"),
        path('updateproduct/<int:dataid>', views.updateproduct, name="updateproduct"),
        path('deleteproduct/<int:dataid>', views.deleteproduct, name="deleteproduct"),

        path('logintest/', views.logintest, name="logintest"),
        path('adminlogin/', views.adminlogin, name="adminlogin"),
        path('adminlogout/', views.adminlogout, name="adminlogout"),



]