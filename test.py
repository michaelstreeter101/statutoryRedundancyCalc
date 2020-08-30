import unittest
import datetime
import calc

class TestExMethods(unittest.TestCase):
    """docstring for TestExMethods."""
    rdndnt_dt = datetime.datetime(2020, 9, 5)

    def test_add_years(self):
        print('test_add_years')
        self.assertEqual(
             calc.add_years(
             datetime.datetime(2014, 2, 27), 2),
             datetime.datetime(2016, 2, 27))

    def test_michael(self):
        print('Michael')
        brth_dt = datetime.datetime(1970, 3, 30)
        strt_dt = datetime.datetime(2018, 10, 14)
        wk_py = 1058
        self.assertEqual( calc.calculate_redundancy(brth_dt, strt_dt, wk_py), 0)

    def test_spyros(self):
        print('Spyros')
        brth_dt = datetime.datetime(1972, 3, 30)
        strt_dt = datetime.datetime(2011, 2, 27)
        wk_py = 1169
        self.assertEqual( calc.calculate_redundancy(brth_dt, strt_dt, wk_py), 14028.00)


if __name__=="__main__":
    unittest.main()
