from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.halamanHome, name = 'home'),
    path('<int:post_id>', views.lengkap_barang, name='lengkap_barang'),
    # path('barang_new', views.input_barang, name='input_barang'),
]