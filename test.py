import unittest
import datetime
import calc

class TestExMethods(unittest.TestCase):
    """docstring for TestExMethods."""

    def test_add_years(self):
        print('test_add_years')
        self.assertEqual(
             calc.add_years(
             datetime.datetime(2014, 2, 27), 2),
             datetime.datetime(2016, 2, 27))

    def test_michael(self):
        print('Michael')
         # This is a completely made up number
        self.assertEqual( calc.calculate_redundancy(rdndnt_dt = datetime.datetime(2020, 9, 25), curr_age = 50, curr_yr = 1, wk_py = 101300), 0)

    def test_vincent(self):
        print('Vincent')
        self.assertEqual( calc.calculate_redundancy(rdndnt_dt = datetime.datetime(2020, 9, 25), curr_age = 49, curr_yr = 10, wk_py = 120100), 1741450)

    def test_joe(self):
        print('Joe Bloggs')
        print('!!!!!!!!!!!!!!!!!!!!!!!')
        self.assertEqual( calc.calculate_redundancy(rdndnt_dt = datetime.datetime(2020, 9, 25), curr_age = 29, curr_yr = 10, wk_py = 67307.69), 639422)


if __name__=="__main__":
    unittest.main()
