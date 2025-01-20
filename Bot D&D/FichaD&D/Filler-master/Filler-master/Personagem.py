#coding=utf-8
from Classes import *
from Situacao import Situacao
from Writer import Writer
import json
import types

def load_personagem(caminho):
	with open(caminho) as json_data:
	    d = json.load(json_data)
	    # print d

	personagem = Personagem(d['nome'], d['atributos']['for'], d['atributos']['dex'], d['atributos']['con'], d['atributos']['int'], d['atributos']['sab'], d['atributos']['car'])

	for classe in d['classes']:
		modul = __import__("Classes")
		class_ = getattr(modul, classe)
		instance = class_(d['classes'][classe])
		personagem.set_class(instance)
	
	return personagem

class Personagem(object):
	"""docstring for Personagem"""
	def __init__(self, nome=None, forca=None, destreza=None, constituicao=None, inteligencia=None, sabedoria=None, carisma=None):
		super(Personagem, self).__init__()
		self.nome = nome
		self.life = 0
		self.nivel = 0
		self.bba = 0
		self.fortitude = 0
		self.reflexos = 0
		self.vontade = 0
		self.classes = {}
		self.atributos = {}
		self.atributos['for'] = forca
		self.atributos['dex'] = destreza
		self.atributos['con'] = constituicao
		self.atributos['int'] = inteligencia
		self.atributos['sab'] = sabedoria
		self.atributos['car'] = carisma

		if self.nome:
			self.atualizar()

	def set_class(self, obj):
		self.classes[type(obj).__name__] = obj
		if self.nome:
			self.atualizar()
		return Situacao(True, "Classe adicionada com sucesso")

	def atualizar(self):
		self.update_personagem()
		self.salvar()

	def update_personagem(self):
		self.life = 0
		self.nivel = 0
		self.bba = 0
		self.fortitude = 0
		self.reflexos = 0
		self.vontade = 0
		for classe in self.classes:
			self.nivel += self.classes[classe].nivel
			self.life += self.classes[classe].nivel*(self.classes[classe].dv + (self.atributos['con']-10)/2)
			self.bba += self.classes[classe].bba
			self.fortitude += self.classes[classe].fortitude
			self.reflexos += self.classes[classe].reflexos
			self.vontade += self.classes[classe].vontade

		self.fortitude += (self.atributos['con']-10)/2
		self.reflexos += (self.atributos['dex']-10)/2
		self.vontade += (self.atributos['sab']-10)/2

	def salvar(self):
		# print "salvou?"
		Writer(self)

	def __str__(self):
		string = "Nome do personagem: " + self.nome
		string += "\n"
		string += "lvl: " + str(self.nivel)
		string += "\t"
		string += "HP: " + str(self.life)
		string += "\n"
		if bool(self.classes):
			string += "classes: "
			for classe in self.classes:
				string += classe + " lvl: " + str(self.classes[classe].nivel)
				string += " | "
			string += "\n"
		string += "Atributos: "
		for atributo in self.atributos:
		 	string += atributo + ": " + str(self.atributos[atributo])
		 	string += "\t"
		string += "\n"
		string += "BBA: " + str(self.bba)
		string += "\n"
		string += "FORT: " + str(self.fortitude) + " | REF: " + str(self.reflexos) + " | VON: " + str(self.vontade)
		return string


# assis = Personagem('Assis', 17, 14, 20, 12, 14, 10)
# assis.set_class(Barbaro(3))
# assis.set_class(Guerreiro(4))
# print assis

# personagem = load_personagem("personagens/Assis.rf")
# print personagem