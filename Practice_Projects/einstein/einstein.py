'''implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.'''

def einstein():
    m = int(input('Insert mass value:'))
    c = 300000000
    E = m*(c**2)
    return E

result = einstein()
print(result)