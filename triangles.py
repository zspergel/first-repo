import math
side1=input('Enter the first side of the right triangle')
side2=input('Enter the second side of the right triangle')
hypo=math.sqrt(int(side1)**2+int(side2)**2)
print(f'Given the first side is {side1} and the second side is {side2} the hypotenuse is {hypo}')