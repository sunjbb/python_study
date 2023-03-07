import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_formatted_name('张', '三')
        self.assertEqual(format_name, '张三')

if __name__ == '__main__':
    unittest.main()