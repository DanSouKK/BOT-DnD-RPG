class Situacao(object):
	"""docstring for Situacao"""
	def __init__(self, status, mensagem):
		super(Situacao, self).__init__()
		self.status = status
		self.mensagem = mensagem
	
	def __str__(self):
		return self.status.__str__()+': '+self.mensagem