import unittest
from name_function import *

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_name_2(self):
        formatted_name = get_formatted_name_v2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_name_3(self):
        formatted_name = get_full_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_last_name_4(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()