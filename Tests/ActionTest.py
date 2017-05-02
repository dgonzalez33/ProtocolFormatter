import unittest
from FormatterSub.Action import Action


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.newelement1 = Action()

    def testCapture(self):
        # w 1.1
        "def getActionResult(self, target): is not the same method regarding parameters with protocol method"
        " it is missing String attribute, String value, STRING key")

if __name__ == '__main__':
    unittest.main()
