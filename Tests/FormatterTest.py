import unittest
import os

from FormatterSub.Formatter import Formatter

class FormatterTest(unittest.TestCase):
	
	def setUp(self):
		self.testFormatter = Formatter(
