import unittest
import os

from FormatterSub.Rule import Rule
from PDMLSub.PDMLManager import pdmlmanager

class RuleTest(unittest.TestCase):

	def setUp(self):
		self.testManager = pdmlmanager("Scripts/dns_query_response2.pdml")
		self.testRule = Rule()
		
	def testapplyRules(self):
		self.testRule.applyRule(self.testManager)
		
		
if __name__ == '__main__':
	unittest.main()
