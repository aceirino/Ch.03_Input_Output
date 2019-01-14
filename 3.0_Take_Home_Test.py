'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________



1. Write a line of code that will print your name.
'''
print("aidan kugley")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?

'''
input("what is your name? ")

'''
3. Predict the ouput of the following lines of code and then test them? Write down your prediction and the output.
print (17/9)
print (17//9)
print (17%9)

predict   test
1.88      1.88
1         1
8         8
'''


'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.

'''
base=float(input("Base: "))
height=float(input("height: "))
area=(base*height)/2
print(area)

'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
a="May the Force be with you!"
print(a)


'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
length=float(input(length: ))
area=(length*length)
print(area)
'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
a=float(input("Enter length a: " ))
b=float(input("Enter length b: " ))
area=(3.14*a*b)
print(area)
'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
n=float(input("moles: "))
V=float(input("volume: "))
T=float(input("temperature: "))
R=8.3144
P=n*R*T/V
print(P)

'''
9. Ask a user for an integer and then print the square root.
'''
a=int(input("enter integer: "))
answer=(a**(.5)
print(answer)

'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
print("May the mass times acceleration be with you!")
a=float(input("mass?: "))
b=float(input("acceleration?: "))
answer=(a*b)
print(answer)
