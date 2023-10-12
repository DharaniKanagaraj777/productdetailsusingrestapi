from django.urls import path
from . import views

urlpatterns =[
    path('',views.Product_list),
    path('product1/<int:pk>',views.Product_detail)
    
]
