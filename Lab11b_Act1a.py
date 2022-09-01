# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab11b_Act1
# Date:         11 29 2021

from math import *
import sympy
def parta(l,w,h,r):
    if(r<min(l/2,w/2)):
        return (l*w*h) - (pi*r**2*h)
    elif(r<sqrt((l**2+w**2))/2):
        H1 = r - l/2
        H2 = r - w/2
        return (l*w*h) - (pi*r**2*h) + 2*h*(r**2*acos(1-H1/r) - (r-H1)*(sqrt(r**2 - (r - H1)**2))) + 2*h*(r**2*acos(1-H2/r) - (r-H2)*(sqrt(r**2 - (r - H2)**2)))
    else:
        return 0

#print(parta(3,3,3,1.6))
#print(parta(1,1,1,.75))