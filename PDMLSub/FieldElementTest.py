import unittest
from FieldElement import fieldelement

class FieldElementTest(unittest.TestCase):
    def setUp(self):
        self.newelement1 = fieldelement()
        self.newelement2 = fieldelement()
        self.newelement3 = fieldelement()
        self.newelement1.set_field_attrib("name", "host1")
        self.newelement1.set_depth_of_indent(1)
        self.newelement2.set_field_attrib("name", "")
        self.newelement2.set_depth_of_indent(-1)
        self.newelement3.set_field_attrib("name", 10)
        self.newelement3.set_depth_of_indent(0)

    def testset_field_attrib(self):
        self.newelement1.set_field_attrib("name", 1)
        #w 1.1
        self.assertEqual(self.newelement1.get_field_attributes_value(0), 1, "wrong value after newelement1 set")
        self.newelement2.set_field_attrib("name", "")
        #w 1.2
        self.assertEqual(self.newelement2.get_field_attributes_value(0), "", "wrong value after newelement2 set")
        self.newelement3.set_field_attrib("name", "host3")
        #w 1.3
        self.assertEqual(self.newelement3.get_field_attributes_value(0), "host3", "wrong value after newelement3 set")



if __name__ == '__main__':
    unittest.main()
#zeke