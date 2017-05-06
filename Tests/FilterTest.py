import unittest
from Filter import Filter

class FilterTest(unittest.TestCase):

	def setUp(self):
		self.newelement1 = Filter()
		self.newelement2 = Filter()
		self.netelement3 = Filter()
		self.newelement1.saveFilter("testFilter")
		self.newelement2.saveFilter("")
		self.newelement3.saveFilter(3)
