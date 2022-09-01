# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab11b_Act1
# Date:         11 29 2021

def partd(fileName):
    csv = open(fileName,'r')
    tsv = open(fileName[:-3]+'tsv','w')
    for next_line in csv:
        node = next_line.strip("\n").split(",")
        tsv.write("\t".join(node))
        tsv.write("\n")
    csv.close()
    tsv.close()
    return "Done!"

#print(partd("CLLWeatherData.csv"))

