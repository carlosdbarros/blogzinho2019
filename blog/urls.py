from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from .views import (
    HomePageView, AuthRegisterView,
    PublicacaoDetailView, PerfilView,
)

app_name='blog'

urlpatterns = [
    # auth
    path('register/', AuthRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # blog
    path('', HomePageView.as_view(), name='home'),
    path(
        'publicacao/<int:pk>/detail/',
        PublicacaoDetailView.as_view(),
        name='publicacao_detail'
    ),

    # Perfil
    path(
        'perfil/<str:slug>',
        PerfilView.as_view(),
        name='perfil'
    )

]