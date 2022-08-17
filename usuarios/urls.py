from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.login, name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('criar-conta/', views.criar_conta, name="criar-conta"),
    path('trocar-senha/', views.TrocarSenha.as_view(), name="troca-senha"),
    re_path(r'^ativar-conta/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.ativar_conta, name='ativar-conta'),
]
