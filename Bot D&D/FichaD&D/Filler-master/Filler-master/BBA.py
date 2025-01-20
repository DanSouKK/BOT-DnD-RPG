import abc

class BBA_Boa(object):
	"""docstring for BBA_Boa"""
	__metaclass__ = abc.ABCMeta
	valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

	@abc.abstractmethod
	def __str__(self):
		raise NotImplementedError('users must define __str__ to use this base class')

class BBA_Ruim(object):
	"""docstring for BBA_Ruim"""
	__metaclass__ = abc.ABCMeta
	valores = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]

	@abc.abstractmethod
	def __str__(self):
		raise NotImplementedError('users must define __str__ to use this base class')