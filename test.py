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
        wk_py = 101300 # This is a completely made up number
        self.assertEqual( calc.calculate_redundancy(brth_dt, strt_dt, wk_py), 0)

    def test_vincent(self):
        print('Vincent')
        brth_dt = datetime.datetime(1972, 3, 30)
        strt_dt = datetime.datetime(2011, 3, 27)
        wk_py = 120100
        self.assertEqual( calc.calculate_redundancy(brth_dt, strt_dt, wk_py), 1501250)

    def test_joe(self):
        print('Joe Bloggs')
        brth_dt = datetime.datetime(1989, 6, 30)
        strt_dt = datetime.datetime(2010, 3, 27)
        wk_py = 67307.69
        print(calc.calculate_redundancy(brth_dt, strt_dt, wk_py))
        print('!!!!!!!!!!!!!!!!!!!!!!!')
        self.assertEqual( calc.calculate_redundancy(brth_dt, strt_dt, wk_py), 639422)


if __name__=="__main__":
    unittest.main()
