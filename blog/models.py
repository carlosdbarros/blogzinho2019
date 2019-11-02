from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE
    )
    seguidores = models.ManyToManyField(
        'Perfil',
        blank=True,
    )
    name = models.CharField("Nome completo", max_length=150)
    avatar = models.ImageField(default='profile01.svg', upload_to='profile_pics')
    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        str_formt = self.name.upper()
        str_formt += f", POSSUI {self.seguidores.count()} SEGUIDORES"
    
        return str_formt


class Publicacao(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Autor",
        on_delete=models.PROTECT
    )
    text = models.TextField('Descrição')
    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        str_formt = f"CRIADO EM {self.created.strftime('%d/%m/%Y')}, "
        str_formt += f"POR {self.author.username}"

        return str_formt


class Comentario(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Autor",
        related_name='author',
        on_delete=models.PROTECT
    )
    resposta = models.ForeignKey(
        'Comentario',
        null = True,
        blank = True,
        verbose_name="Resposta",
        on_delete=models.PROTECT
    )
    publicacao = models.ForeignKey(
        Publicacao,
        verbose_name="Publicação",
        on_delete=models.PROTECT
    )
    text = models.TextField('Comentário')
    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
    
    def __str__(self):
        str_formt = f"{self.created.strftime('%m/%d/%Y, %H:%M:%S')} - "
        str_formt += f"COMETÁRIO FEITO POR: {self.author.username.upper()} - "
        str_formt += 'POSSUI RESPOSTA' if self.resposta else 'NÂO POSSUI RESPOSTA'

        return str_formt
