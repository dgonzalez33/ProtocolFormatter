import unittest
from FileSub.Tshark_Handler import Tshark_Handler


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.newelement1 = Tshark_Handler()

    def testCapture(self):
        self.newelement1.createPDML("Scripts/cubic.pdml")
        # w 1.1
        self.assertEqual(self.newelement1.createPDML("Scripts/cubic.pdml"), ("Scripts/cubic.pdml"), "file wasnt created")

if __name__ == '__main__':
    unittest.main()
