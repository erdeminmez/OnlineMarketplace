from django.urls import path

from . import views

app_name="item"

urlpatterns = [
    path('<int:item_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:pk>/delete', views.delete, name='delete'),
]