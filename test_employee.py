import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):    # run it code before every single test (we use this instead of declare it on every test case)
        self.emp_1 = Employee('Voramet', 'Chunvattananon', 200000)
        self.emp_2 = Employee('Michael', 'Scott', 150000)

    def tearDown(self):  # run it code after every single test
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Voramet.Chunvattananon@email.com')
        self.assertEqual(self.emp_2.email, 'Michael.Scott@email.com')

        self.emp_1.first = 'Mc'
        self.emp_2.first = 'Mike'

        self.assertEqual(self.emp_1.email, 'Mc.Chunvattananon@email.com')
        self.assertEqual(self.emp_2.email, 'Mike.Scott@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Voramet Chunvattananon')
        self.assertEqual(self.emp_2.fullname, 'Michael Scott')

        self.emp_1.first = 'Mc'
        self.emp_2.first = 'Mike'

        self.assertEqual(self.emp_1.fullname, 'Mc Chunvattananon')
        self.assertEqual(self.emp_2.fullname, 'Mike Scott')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 210000)
        self.assertEqual(self.emp_2.pay, 157500)


if __name__ == '__main__':
    unittest.main()