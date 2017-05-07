import unittest
import os

from FormatterSub.Rule import Rule
from PDMLSub.PDMLManager import pdmlmanager

class RuleTest(unittest.TestCase):

	def setUp(self):
		self.testManager = pdmlmanager()
		self.testRule = Rule()
		
	def testapplyRules(self):
		self.testRule.applyRules(testManager)
		
		
if __name__ == '__main__':
	unittest.main()
