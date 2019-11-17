from django.contrib import admin
from .models import Comentario, Perfil, Publicacao

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display= ['author','created', 'updated']
    readonly_fields = ['created','updated']
    search_fields = ['author__username']


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['name', 'created','updated']
    readonly_fields = ['created','updated']
    filter_horizontal = ['seguidores']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    search_fields = ['author__username']
