from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


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
        str_format = self.name.upper()
        str_format += f", POSSUI {self.seguidores.count()} SEGUIDORES"
        return str_format


class Publicacao(models.Model):
    titulo = models.CharField("Título", max_length=100)
    author = models.ForeignKey(
        User,
        verbose_name="Autor",
        on_delete=models.PROTECT
    )
    text = models.TextField('Descrição')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def save(self, *args, **kwargs):
        if len(self.titulo) > 1:
            self.slug = slugify(self.titulo)

        super(Publicacao, self).save(*args, **kwargs)

    def __str__(self):
        str_format = f"CRIADO EM {self.created.strftime('%d/%m/%Y')}, "
        str_format += f"POR {self.author.username}"

        return str_format


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
        str_format = f"{self.created.strftime('%m/%d/%Y, %H:%M:%S')} - "
        str_format += f"COMETÁRIO FEITO POR: {self.author.username.upper()} - "
        str_format += 'POSSUI RESPOSTA' if self.resposta else 'NÂO POSSUI RESPOSTA'

        return str_format
