from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Usuário",
        on_delete=models.PROTECT
    )
    name = models.CharField("Nome completo", max_length=150)
    avatar = models.ImageField(default='profile01.svg', upload_to='profile_pics')
    seguidores = models.ManyToManyField("Perfil", verbose_name="Seguidores")

class Comentario(models.Model):
    author = models.ForeignKey(
        Perfil,
        verbose_name="Autor",
        related_name='autor',
        on_delete=models.PROTECT
    )
    resposta = models.ForeignKey(
        'Comentario',
        verbose_name="Resposta",
        related_name='resposta',
        on_delete=models.PROTECT
    )
    text = models.TextField('Comentário')

class Publicao(models.Model):
    author = models.ForeignKey(
        Perfil,
        verbose_name="Autor",
        related_name='autor',
        on_delete=models.PROTECT
    )
    comentario = models.ForeignKey(
        'Comentario',
        verbose_name="Descrição",
        on_delete=models.CASCADE
    )
    descricao = models.TextField('Descrição')
    image = models.ImageField(default='default.png', upload_to='posts')