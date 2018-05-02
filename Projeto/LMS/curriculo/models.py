from django.db import models

# Create your models here.

class Alunos(models.Model):
    login = models.CharField("Login", max_length=50)
    senha = models.CharField("Senha", max_length=50)
    nome = models.CharField("Nome", max_length=100)
    email = models.CharField("Email", max_length=100)
    celular = models.CharField("Celular", max_length=20)
    dt_expiracao = models.DateField("Data Expiracao", max_length=10)
    ra = models.CharField("RA", max_length=7)
    foto = models.CharField("Foto", null=True, blank=True, max_length=100)

    def __str__(self):
        return self.login

class Professor(models.Model):
    login = models.CharField("Login", max_length=50)
    senha = models.CharField("Senha", max_length=50)
    nome = models.CharField("Nome", max_length=100)
    email = models.CharField("Email", max_length=100)
    celular = models.CharField("Celular", max_length=20)
    dt_expiracao = models.DateField("Data Expiracao", max_length=10)
    apelido = models.CharField("Apelido", max_length=25)

    def __str__(self):
        return self.login
		
class Coordenador(models.Model):
    login = models.CharField("Login", max_length=50)
    senha = models.CharField("Senha", max_length=50)
    nome = models.CharField("Nome", max_length=100)
    email = models.CharField("Email", max_length=100)
    celular = models.CharField("Celular", max_length=20)
    dt_expiracao = models.DateField("Data Expiracao", max_length=10)

    def __str__(self):
        return self.login
	
class Disciplina(models.Model):
	ID = models.AutoField("ID", primary_key=True)
	Nome = models.CharField("Nome", max_length=255)
	Data = models.DateField("Data")
	Status = models.CharField("Status", max_length=255)
	PlanoDeEnsino = models.CharField("PlanoDeEnsino", max_length=255)
	CargaHoraria = models.SmallIntegerField("CargaHoraria")
	Competencias = models.CharField("Competencias", max_length=255)
	Habilidades = models.CharField("Habilidades", max_length=255)
	Ementa = models.CharField("Ementa", max_length=255)
	ConteudoProgramatico = models.CharField("ConteudoProgramatico", max_length=255)
	BibliografiaBasica = models.CharField("BibliografiaBasica", max_length=255)
	BibliografiaComplementar = models.CharField("BibliografiaComplementar", max_length=255)
	PercentualPratico = models.SmallIntegerField("PercentualPratico") 
	PercentualTeorico = models.SmallIntegerField("PercentualTeorico")
	IdCoordenador = models.ForeignKey('Coordenador', on_delete=models.DO_NOTHING)
	
	def __str__(self):
		return self.Nome

class Curso(models.Model):
    nome = models.CharField("Nome", max_length=100)
    def __str__(self):
        return self.nome
		
class DisciplinaOfertada(models.Model):
	ID = models.AutoField("ID", primary_key=True)
	IdCoordenador = models.ForeignKey('Coordenador', on_delete=models.DO_NOTHING)
	DtInicioMatricula = models.DateField("DtInicioMatricula", null=True)
	DtFimMatricula = models.DateField("DtFimMatricula", null=True)
	IdDisciplina = models.ForeignKey('Disciplina', on_delete=models.DO_NOTHING)
	IdCurso = models.ForeignKey('Curso', on_delete=models.DO_NOTHING)
	Ano = models.SmallIntegerField("Ano")
	Semestre = models.SmallIntegerField("Semestre")
	Turma = models.CharField("Turma", max_length=255)
	IdProfessor = models.ForeignKey('Professor', on_delete=models.DO_NOTHING, null=True)
	Metodologia = models.CharField("Metodologia", max_length=255, null=True)
	Recursos = models.CharField("Recursos", max_length=255, null=True)
	CriterioAvaliacao = models.CharField("CriterioAvaliacao", max_length=255, null=True)
	PlanoDeAulas = models.CharField("PlanoDeAulas", max_length=255, null=True)
	
	def __str__(self):
		return self.ID
	
class Mensagem(models.Model):
    assunto = models.CharField("Assunto", max_length=255)
    referencia = models.CharField("Referencia", max_length=255)
    conteudo = models.CharField("Conteudo", max_length=255)
    status = models.CharField("Status", max_length=50)
    dtEnvio = models.DateTimeField("Data Envio", max_length=10)
    dtResposta = models.DateField("Data Resposta", max_length=10)
    resposta  = models.CharField("Resposta", max_length=255)
    Alunos = models.ForeignKey('Alunos', on_delete=models.CASCADE)
    professor=models.ForeignKey('Professor', on_delete=models.CASCADE)
    def __str__(self):
        return self.assunto
		
class Pessoa(models.Model):
	Nome = models.CharField("Nome", max_length=255)