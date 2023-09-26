from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.hello),
    path('db/', views.db),
    path('add/', views.add),
    path('update/<product_id>', views.update),
    path('delete/<product_id>', views.delete),
]