import unittest
import os
from FileSub.Capture import Capture

class CaptureTest(unittest.TestCase):
    def setUp(self):
        self.newelement1 = Capture()
        #self.newelement2 = capture()
        #self.newelement3 = capture()
        self.newelement1.createCapture("Scripts/cubic.pdml")
        #self.newelement2.
       # self.newelement3.
    def testCapture(self):
        self.newelement1.createCapture("Scripts/cubic.pdml")
        file = open("Scripts/cubic.pdml")
        #w 1.1
        self.assertEqual(self.newelement1.createCapture("Scripts/cubic.pdml"), ("Scripts/cubic.pdml" and file) ,"wrong file path return or PDML not returned")
       # self.newelement2.set_field_attrib("name", "")
        #w 1.2
      #  self.assertEqual(self.newelement2.get_field_attributes_value(0), "", "wrong value after newelement2 set")
       # self.newelement3.set_field_attrib("name", "host3")
        #w 1.3
      #  self.assertEqual(self.newelement3.get_field_attributes_value(0), "host3", "wrong value after newelement3 set")



if __name__ == '__main__':
    unittest.main()
