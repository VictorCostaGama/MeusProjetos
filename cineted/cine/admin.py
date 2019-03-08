from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(produtora)
class ProdutoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)


@admin.register(filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'duracao', 'etaria', 'produtora', 'nota_imdb',)
    list_filter = ('titulo', 'sinopse', 'duracao', 'etaria', 'produtora', 'nota_imdb',)
    search_fields = ('titulo',)

    def descricao(self, obj):
        desc = obj.sinopse
        if desc:
            if len(desc) > 40:
                return '%s...' % desc[:50]
        return desc


@admin.register(ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)


@admin.register(elenco)
class ElencoAdmin(admin.ModelAdmin):
    list_display = ('ator', 'filme')
    list_filter = ('ator', 'filme',)
    search_fields = ('ator',)


@admin.register(diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)


@admin.register(conselho)
class ConselhoAdmin(admin.ModelAdmin):
    list_display = ('diretor', 'filme',)
    list_filter = ('diretor', 'filme',)
    search_fields = ('diretor',)


@admin.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('genero',)
    list_filter = ('genero',)
    search_fields = ('genero',)


@admin.register(grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('genero', 'filme',)
    list_filter = ('genero', 'filme',)
    search_fields = ('genero',)


@admin.register(conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('tema',)
    list_filter = ('tema',)
    search_fields = ('tema',)


@admin.register(teor)
class TeorAdmin(admin.ModelAdmin):
    list_display = ('tema', 'filme',)
    list_filter = ('tema', 'filme',)
    search_fields = ('tema',)


@admin.register(cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'shopping',)
    list_filter = ('empresa', 'shopping',)
    search_fields = ('empresa',)
    

@admin.register(exibicao)
class ExibicaoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'filme',)
    list_filter = ('empresa', 'filme',)
    search_fields = ('empresa',)


@admin.register(sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('sala',)
    list_filter = ('sala',)
    search_fields = ('sala',)


@admin.register(recinto)
class RecintoAdmin(admin.ModelAdmin):
    list_display = ('sala', 'cinema',)
    list_filter = ('sala', 'cinema',)
    search_fields = ('sala',)


@admin.register(versao)
class VersaoAdmin(admin.ModelAdmin):
    list_display = ('versao',)
    list_filter = ('versao',)
    search_fields = ('versao',)


@admin.register(formato)
class FormatoAdmin(admin.ModelAdmin):
    list_display = ('formato',)
    list_filter = ('formato',)
    search_fields = ('formato',)


@admin.register(tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('tecnologia',)
    list_filter = ('tecnologia',)
    search_fields = ('tecnologia',)


@admin.register(data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('data',)
    list_filter = ('data',)
    search_fields = ('data',)


@admin.register(sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ('sala', 'filme', 'versao', 'formato', 'tecnologia', 'data',)
    list_filter = ('sala', 'filme', 'versao', 'formato', 'tecnologia', 'data',)
    search_fields = ('sala',)


@admin.register(horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora', 'sessao',)
    list_filter = ('hora', 'sessao',)
    search_fields = ('hora',)


@admin.register(calendario)
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario',)
    list_filter = ('data', 'horario',)
    search_fields = ('data',)
