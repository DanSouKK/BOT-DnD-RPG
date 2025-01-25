#coding=utf-8
import types
import abc
from Resist import Resist_Boa, Resist_Ruim
from BBA import BBA_Boa, BBA_Ruim

class Class(object):
	"""docstring for Class"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __str__(self):
		raise NotImplementedError('users must define __str__ to use this base class')

	def __init__(self, nivel):
		super(Class, self).__init__()
		self.nivel = nivel
		
		self.bba = type(self).bba[(nivel-1)]

		self.fortitude = type(self).fortitude[(self.nivel-1)]
		self.reflexos = type(self).reflexos[(self.nivel-1)]
		self.vontade = type(self).vontade[(self.nivel-1)]
	
	def __str__(self):
		string = "nv: " + str(self.nivel) + " bba: " + str(self.bba)
		string += "\nFOR: " + str(self.fortitude)
		string += "\nREF: " + str(self.reflexos)
		string += "\nVON: " + str(self.vontade)
		return string

class Barbaro(Class):
	"""docstring for Barbaro"""
	nome = "Bárbaro"
	dv = 12
	bba = BBA_Boa.valores
	pericias = ["Adestrar Animais", "Cavalgar", "Escalar", "Intimidação", "Natação", "Ofícios", "Ouvir", "Saltar", "Sobrevivência"]

	pericia_por_lvl = 4

	fortitude = Resist_Boa.valores
	reflexos = Resist_Ruim.valores
	vontade = Resist_Ruim.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Bardo(Class):
	"""docstring for Bardo"""
	nome = "Bardo"
	dv = 6
	bba = BBA_Ruim.valores
	pericias = []

	pericia_por_lvl = 6

	fortitude = Resist_Ruim.valores
	reflexos = Resist_Boa.valores
	vontade = Resist_Boa.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Clerigo(Class):
	"""docstring for Clerigo"""
	nome = "Clérigo"
	dv = 8
	bba = BBA_Ruim.valores
	pericias = []

	pericia_por_lvl = 2

	fortitude = Resist_Boa.valores
	reflexos = Resist_Ruim.valores
	vontade = Resist_Boa.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Druida(Class):
	"""docstring for Druida"""
	nome = "Druida"
	dv = 8
	bba = BBA_Ruim.valores
	pericias = []

	pericia_por_lvl = 4

	fortitude = Resist_Boa.valores
	reflexos = Resist_Ruim.valores
	vontade = Resist_Boa.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Guerreiro(Class):
	"""docstring for Guerreiro"""
	nome = "Guerreiro"
	dv = 10
	bba = BBA_Boa.valores
	pericias = []

	pericia_por_lvl = 2

	fortitude = Resist_Boa.valores
	reflexos = Resist_Ruim.valores
	vontade = Resist_Ruim.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Ladino(Class):
	"""docstring for Ladino"""
	nome = "Ladino"
	dv = 6
	bba = BBA_Ruim.valores
	pericias = []

	pericia_por_lvl = 8

	fortitude = Resist_Ruim.valores
	reflexos = Resist_Boa.valores
	vontade = Resist_Ruim.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Mago(Class):
	"""docstring for Mago"""
	nome = "Mago"
	dv = 2
	bba = BBA_Ruim.valores
	pericias = []

	pericia_por_lvl = 6

	fortitude = Resist_Ruim.valores
	reflexos = Resist_Ruim.valores
	vontade = Resist_Boa.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Monge(Class):
	"""docstring for Monge"""
	nome = "Monge"
	dv = 8
	bba = BBA_Ruim.valores
	pericias = []

	pericia_por_lvl = 4

	fortitude = Resist_Boa.valores
	reflexos = Resist_Boa.valores
	vontade = Resist_Boa.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Paladino(Class):
	"""docstring for Paladino"""
	nome = "Paladino"
	dv = 10
	bba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	pericias = []

	pericia_por_lvl = 2

	fortitude = Resist_Boa.valores
	reflexos = Resist_Ruim.valores
	vontade = Resist_Ruim.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)

class Ranger(object):
	"""docstring for Ranger"""
	nome = "Ranger"
	dv = 8
	bba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	pericias = ["Adestrar Animais", "Cavalgar", "Concentração", "Conhecimento (geografia)", "Conhecimento (masmorras)", "Conhecimento (natureza)", "Cura", "Escalar", "Esconder-se", "Furtividade", "Natação", "Obeservar", "Ofícios", "Ouvir", "Procurar", "Profissão", "Saltar", "Sobrevivência", "Usar Cordas"]

	pericia_por_lvl = 6

	fortitude = Resist_Boa.valores
	reflexos = Resist_Boa.valores
	vontade = Resist_Ruim.valores

	def __init__(self, nivel):
		Class.__init__(self, nivel)