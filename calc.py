import datetime

def add_years(d, years):
    """Return a date, d, with years added on.
    Ref: https://stackoverflow.com/questions/15741618/add-one-year-in-current-date-python"""
    try:
        return d.replace(year = d.year + years)
    except ValueError: # 29 Feb, 31 Sep etc.
        return d + (datetime.datetime.date(d.year + years, 1, 1) - datetime.datetime.date(d.year, 1, 1))

def calculate_redundancy(rdndnt_dt, curr_age, curr_yr, wk_py):
    """
    Original author: MWS
    Creation date: 2020-00-11
    Purpose: given 4 parameters,
        What date were you made redundant?
        How old were you on the date you were made redundant?
        How many years have you worked for your employer? and
        What is your weekly pay before tax and any other deductions?
    """
    print("Redundant on: {}".format(rdndnt_dt))
    print("Current age: {}".format(curr_age))
    print("Employed for {} years".format(curr_yr))
    tot_ent : int = 0 # return Value
    if curr_yr < 2:
        print('You do not qualify for statutory redundancy until you have been employed for 2 years or longer.')

    else:
        # 1/2 week's pay for each full year you were under 21,
        # One week's pay for each full year you were 22 or older and under 41, and
        # 1 1/2 week's pay for each full year you were 41 or older.

        # First off, convert wk_py from an integer number of pennies, to tenths of a penny.
        wk_py : int = int(wk_py * 10)

        # Calculate the three different rates
        ent : tuple = (int(wk_py * 0.5), wk_py, int(wk_py * 1.5)) # should be a tuple of 3 ints
        
        # Calculate total entitlement, capped at 20 years
        for y in range(min([20, curr_yr])):
            if curr_age < 21:
                curr_ent = ent[0]
            elif 21 <= curr_age < 41:
                curr_ent = ent[1]
            elif curr_age >= 41:
                curr_ent = ent[2]
            else:
                print('ERROR! Please contact support! Error:{}'.format(curr_age))

            print("Year: {}, age:{}, amount: {:06.2f}".format(curr_yr-y, curr_age, curr_ent/1000))
            tot_ent += curr_ent
            curr_age -= 1

    # print the result
    if 20 < curr_yr:
        print("Capped at 20 years")
    print('Sum total of all entitlement: £{:06.2f}'.format(tot_ent/1000))
    print(' ')

    # Convert back from tenths of a penny to pennies for the calling program
    return int(tot_ent/10)

    # =================================================================================================================

def main():
    print('Joe Bloggs')
    wk_py : float = 67307.69 # £637.0769 per week, in pennies.
    calculate_redundancy(rdndnt_dt = datetime.datetime(2020, 9, 25), curr_age = 29, curr_yr = 10, wk_py = wk_py)

if __name__=="__main__":
    main()
