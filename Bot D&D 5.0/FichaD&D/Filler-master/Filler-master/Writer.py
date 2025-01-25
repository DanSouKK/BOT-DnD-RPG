import json

class Writer(object):
	"""docstring for Writer"""
	def __init__(self, obj):
		super(Writer, self).__init__()
		self.file = open("personagens/"+obj.nome+".rf", 'w')
		# print obj
		js = {}
		js['nome'] = obj.nome
		js['classes'] = {}
		js['atributos'] = {}
		for classe in obj.classes:
			js['classes'][classe] = obj.classes[classe].nivel
		for atributo in obj.atributos:
			js['atributos'][atributo] = obj.atributos[atributo]
		self.file.write(json.dumps(js))
		self.file.close()	