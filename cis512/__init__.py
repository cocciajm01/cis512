print ('hello world')


import csv as csv

town = []
state= []
zip = []


f = open("/home/JuliaCoccia/Documents/SFHFCLData.csv")
csv.reader(f)
for line in f:
    if "******" not in line:
        splitline = line.split(',')
        if len(splitline[0])<20:

            town.append(splitline[0])
            state.append(splitline[1])
            zip.append(splitline[2])
            #print(splitline)

print (town)
