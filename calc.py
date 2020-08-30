#import unittest
import datetime

def add_years(d, years):
    """Return a date, d, with years added on.
    Ref: https://stackoverflow.com/questions/15741618/add-one-year-in-current-date-python"""
    try:
        return d.replace(year = d.year + years)
    except ValueError: # 29 Feb, 31 Sep etc.
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


def calculate_redundancy(brth_dt, strt_dt, wk_py, rdndnt_dt = datetime.datetime(2020, 9, 5)):
    """Original author: MWS
    Creation date: 2020-08-20
    Purpose: given DOB, Start date with the company, weekly pay, and date of redundancy,
    return the statutory redundancy payout value (uncapped).
    Show all your working so the reader can be confident the answer is correct."""

    tdy_dt = datetime.datetime.today() # Note: not used in the calculation; only used to supress printing of future dates.
    print('Born: {}'.format(brth_dt.strftime("%d %b %Y")))

    brth21_dt = add_years(brth_dt, 21) # Note: this variable is not used anywhere else.
    if brth21_dt < tdy_dt:
        print('21 on: {}'.format(brth21_dt.strftime("%d %b %Y")))

    brth41_dt = add_years(brth_dt, 41) # Note: this variable is not used anywhere else.
    if brth41_dt < tdy_dt:
        print('41 on: {}'.format(brth41_dt.strftime("%d %b %Y")))

    print('Started on: {}'.format(strt_dt.strftime("%d %b %Y")))

    curr_age = (strt_dt - brth_dt).days//365
    print('Age at time of joining: {}'.format(curr_age))

    strt2_dt = add_years(strt_dt, 2)
    if strt2_dt < tdy_dt:
        print('2nd work anniversary on: {}'.format(strt2_dt.strftime("%d %b %Y")))

    srvc = (rdndnt_dt-strt_dt).days//365
    print('You have {} complete years of service'.format(srvc))

    print('Assuming your position becomes redundant on {}, the payout would be calculated as follows...'.format(rdndnt_dt.strftime("%d %b %Y")))

    tot_ent = 0
    if strt2_dt > rdndnt_dt:
        print('You do not qualify for statutory redundancy until you have been employed for 2 years or longer.')

    else:
        # 1/2 week's pay for each full year you were under 21,
        # One week's pay for each full year you were 22 or older and under 41, and
        # 1 1/2 week's pay for each full year you were 41 or older.

        curr_year = strt_dt
        curr_ent = 0
        for s in range (srvc):

            if curr_age < 21:
                curr_ent = wk_py * 0.5
            elif 21 < curr_age < 41:
                curr_ent = wk_py
            elif 41 <= curr_age:
                curr_ent = wk_py *1.5
            else:
                print('ERROR! Please contact support! Error:{}'.format(curr_age))

            print("Year: {:2d}, SOY date: {}, Age: {}, Entitlement: {:06.2f}".format(s+1, curr_year.strftime("%d %b %Y"), curr_age, curr_ent))
            tot_ent += curr_ent
            curr_year = add_years(curr_year, 1)
            curr_age += 1

    print('Sum total of all entitlement: £{:06.2f}'.format(tot_ent))
    print(' ')

    return tot_ent

def main():
    print('Michael')
    brth_dt = datetime.datetime(1970, 3, 30)
    strt_dt = datetime.datetime(2018, 10, 14)
    wk_py = 1058
    calculate_redundancy(brth_dt, strt_dt, wk_py)

if __name__=="__main__":
    main()
#    unittest.main()