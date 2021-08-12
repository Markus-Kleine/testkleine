from django.urls import path
from prog1.views import home, test, create, user_list, createartikel, ArtikelListView, artikel_detail

urlpatterns = [
    path('', home, name='home'),
    path('test', test, name='test'),
    path('create_user', create, name='user_create'),
    path('user_list', user_list, name='user_list'),
    path('create_artikel', createartikel, name='artikel_create'),
    path('artikel_list', ArtikelListView.as_view(), name='artikel_list'),
    path('artikel_detail', artikel_detail, name='artikel_detail'),
]

