Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> weight = float(input('Put Your weight in Kg: '))
... height = float(input('Put your height in M: '))
... calculation = weight/(height**2)
... print('Your BMI is {:.1f}'.format(calculation))
... if calculation <= 18.5:
...     print('You are underweight')
... elif calculation >= 18.5 and calculation <=25:
...     print('You are in the ideal weight')
... elif calculation >= 25 and calculation <=30:
...     print('You are overweight')
... elif calculation >= 30 and calculation <=40:
...     print('you are obese')
... elif calculation >= 40:
