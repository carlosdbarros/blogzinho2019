# https://docs.djangoproject.com/en/2.2/topics/http/urls/

from django.contrib import admin
from django.urls import path, include
from django.urls.base import reverse_lazy
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        RedirectView.as_view(
            url=reverse_lazy(
                'blog:home'
            ),
            permanent=False
        ),
        name="home"
    ),
    path(
        'blog/',
        include(
            'blog.urls',                
            namespace='blog'
        ),
        name='blog'
    ),
      path(
        '',
        include(
            'blog.urls',
            namespace='publicacao'
        ),
        name='publicacao'
    ),
]