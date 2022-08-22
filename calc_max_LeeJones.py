# 2.9.2 PROJECT:  create a new calc_max_yourname.py file.
# Lee Jones
# I took your advice in shortening my file path name and moved my files to the root C: in a folder named PyFiles

"""Find the minimum and maximum of three values."""

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

minimum = min(number1, number2, number3)
maximum = max(number1, number2, number3)

print('Minimum value is', minimum)
print('Maximum value is', maximum)