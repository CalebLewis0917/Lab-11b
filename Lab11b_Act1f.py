# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab11b_Act1
# Date:         11 29 2021

def partf(list1,list2):
    vList = []
    for i in range(len(list1)-1):
        vList.append((list2[i+1]-list2[i])/(list1[i+1]-list1[i]))
    return vList

#print(partf([0,1,2,3,4],[0,10,30,100,1000]))