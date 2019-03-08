from django.db import models

# Create your models here.
class produtora(models.Model):
    nome = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.nome

class filme(models.Model):
    titulo = models.CharField(max_length=250, unique=True)
    sinopse = models.TextField(blank=True, null=True)
    trailer = models.CharField(max_length=250)
    imagem = models.CharField(max_length=250)
    nota_imdb = models.CharField(max_length=10)
    bilheteria = models.CharField(max_length=100)
    produtora = models.ForeignKey(produtora, on_delete=models.CASCADE)
    duracao = models.CharField(max_length=10)
    etaria = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

class ator(models.Model):
    nome = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.nome

class elenco(models.Model):
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(ator, on_delete=models.CASCADE)

    def __str__(self):
        return self.ator + ' - ' + self.filme


class diretor(models.Model):
    nome = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.nome


class conselho(models.Model):
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)
    diretor = models.ForeignKey(diretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.diretor + ' - ' + self.filme


class categoria(models.Model):
    genero = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.genero


class grupo(models.Model):
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)
    genero = models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.filme + ' - ' + self.genero


class conteudo(models.Model):
    tema = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.tema


class teor(models.Model):
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)
    tema = models.ForeignKey(conteudo, on_delete=models.CASCADE)

    def __str__(self):
        return self.filme + ' - ' + self.tema


class cinema(models.Model):
    empresa = models.CharField(max_length=50, unique=True)
    shopping = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.empresa + ' - ' + self.shopping


class exibicao(models.Model):
    empresa = models.ForeignKey(cinema, on_delete=models.CASCADE)
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.empresa) + ' - ' + str(self.filme)


class sala(models.Model):
    sala = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.sala


class recinto(models.Model):
    sala = models.ForeignKey(sala, on_delete=models.CASCADE)
    cinema = models.ForeignKey(cinema, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sala) + ' - ' + str(self.cinema)


class versao(models.Model):
    versao = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.versao


class formato(models.Model):
    formato = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.formato


class tecnologia(models.Model):
    tecnologia = models.CharField(max_length=30, unique=True, null=True)

    def __str__(self):
        return self.tecnologia

class data(models.Model):
    data = models.DateField()

    def __str__(self):
        return str(self.data)


class sessao(models.Model):
    sala = models.ForeignKey(sala, on_delete=models.CASCADE)
    filme = models.ForeignKey(filme, on_delete=models.CASCADE)
    versao = models.ForeignKey(versao, on_delete=models.CASCADE)
    formato = models.ForeignKey(formato, on_delete=models.CASCADE)
    tecnologia = models.ForeignKey(tecnologia, on_delete=models.CASCADE, null=True)
    data = models.ForeignKey(data, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sala) + ' - ' + str(self.filme) + ' - ' + str(self.versao) + ' - ' + str(self.formato)


class horario(models.Model):
    hora = models.CharField(max_length=20, unique=True)
    sessao = models.ForeignKey(sessao, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sessao) + ' - ' + str(self.hora)


class calendario(models.Model):
    data = models.ForeignKey(data, on_delete=models.CASCADE)
    horario = models.ForeignKey(horario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.data) + ' - ' + str(self.horario)