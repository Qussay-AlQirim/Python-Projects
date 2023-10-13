'''Implement a program that ask for the price of a meal and percentage of tip and the determines the amount of tip to pay'''

def main():
    dollars = dollars_to_float(input('How much was the meal?').replace('$', ''))
    percent = percent_to_float(input('What percentage would you like to tip?').replace('%', ''))
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')


def dollars_to_float(d):
    '''convert the string to float'''
    # Convert to float
    d = round(float(d),1)
    return d

def percent_to_float(p):
    '''Convert the string float'''
    # Convert to float
    p = round(float(p),2)

    # Convert to decimal
    p = p/100
    return p

main()
