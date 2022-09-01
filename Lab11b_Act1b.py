# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab11b_Act1
# Date:         11 29 2021

def partb(list1,list2,list3):
    profits = []
    for i in range(len(list1)):
        profits.append(list3[i]-list2[i])
    maxProfit = max(profits) 
    maxdex = profits.index(maxProfit)
    return(list1[maxdex],maxProfit)

#print(partb(['a','b','c'],[100,200,2000],[200,400,1900]))