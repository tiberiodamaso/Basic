from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.login, name="login"),
    path('criar-conta/', views.criar_conta, name="criar_conta"),
    path(r'^ativar-conta/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.ativar_conta, name='ativar-conta'),
]
