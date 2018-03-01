import csv
import os
monthsCount = 0
TotalRevenue = 0
path = input("Enter your file's path: ")
fName = input("Enter your file's name:")
csvPath = os.path.join(path, fName)
with open(csvPath, newline='') as csvfile:
    csvReader = csv.reader (csvfile, delimiter = ',')
    next (csvfile)
    previousRow=0
    Diff=0
    diffInc = 0
    diffDec = 0
    for rows in csvReader:
        monthsCount = monthsCount+1
        TotalRevenue = float(TotalRevenue) + float(rows[1])
        Diff = float(rows[1]) - float(previousRow)
        previousRow =rows[1]
        if Diff>diffInc:
            diffInc = Diff
            IncDate = rows[0]
        else:
            diffDec = Diff
            DecDate = rows[0]
AverageRevenueChange=  TotalRevenue/monthsCount 
print("Total Months: " + str(monthsCount))
print("Total Revenue: " + str(TotalRevenue))
print("Average Revenue Change: " + str(AverageRevenueChange))
print("Greatest Increase in Revenue: " + str(IncDate) + " (" + str(diffInc) + ")")
print("Greatest Decrease in Revenue: " + str(DecDate) + " (" + str(diffDec) + ")")