import unittest
import sys

sys.path.insert(0, '../')
from FormatterSub.Filter import Filter

class FilterTest(unittest.TestCase):

	def setUp(self):
		self.newfilter1 = Filter()
		self.newfilter2 = Filter()
		self.newfilter3 = Filter()
		
		
	def test_saveFilter(self):
		self.newfilter1.saveFilter("testFilter")
		self.newfilter2.saveFilter("")
		self.newfilter3.saveFilter("3")
		
		self.assertEqual(self.newfilter1.fileExists("testFilter"),1,"Filter Exists")
		
		self.assertEqual(self.newfilter2.fileExists(""),1,"Filter Exists")
		
		self.assertEqual(self.newfilter3.fileExists("3"),0,"Filter does not exist")
		
		
if __name__ == '__main__':
	unittest.main()
