from django.db import models

class Porteiro(models.Model):
	DEFICIENTE = (
		('sim','Sim'),
		('nao','Nao'),
		)
	TURNO = (
		('manha','Manha'),
		('tarte','Tarde'),
		('noite','Noite'),
		)
	nome = models.CharField(max_length=50,null=True)
	cpf = models.CharField(max_length=11,null=True)
	rg = models.CharField(max_length=11,null=True)
	email = models.CharField(max_length=50,null=True)
	telefone = models.CharField(max_length=11,null=True)
	data_de_nascimento = models.CharField(max_length=11,null=True)
	cidade = models.CharField(max_length=50,null=True)
	bairro = models.CharField(max_length=50,null=True)
	rua = models.CharField(max_length=50,null=True)
	numero_da_residencia = models.CharField(max_length=50,null=True)
	turno =  models.CharField(max_length=5,choices = TURNO,null=True)
	deficiente = models.CharField(max_length=3, choices = DEFICIENTE,null=True)
	image = models.ImageField(upload_to='media',null=True)
	def __str__(self):
		return self.nome