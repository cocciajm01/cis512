import csv

import numpy as np
import matplotlib.pyplot as plt


myFile = open("/home/JuliaCoccia/Documents/testFile.csv", 'rt')
reader = csv.reader(myFile)
myList = []
for row in reader:
    myList.append(row)
myFile.close()
myArray = np.asarray(myList)
bugsInd = np.flatnonzero(myArray[0, :] == 'bugs')
bugs = myArray[1:, bugsInd].astype(np.float)
print(myList)
frogInd = np.flatnonzero(myArray[0, :] == 'frog')
frog = myArray[1:, frogInd].astype(np.float)
myFit = np.polyfit(bugs.squeeze(), frog.squeeze(), 1, None, True, None, True)

print(myFit)
frogPred = myFit[0][0] * bugs + myFit[0][1]


fig_myFit = plt.figure()
ax_myFit = fig_myFit.add_subplot(111)
bugsvsfrog = ax_myFit.plot(bugs, frog, 'o', color='r', label='Original Data')
linearFit = ax_myFit.plot(bugs, frogPred, color='k', label='Linear Fit')
ax_myFit.grid(True)
ax_myFit.set_xlabel('bug units')
ax_myFit.set_ylabel('frog units')
ax_myFit.set_title('bugs vs. frog')
ax_myFit.legend()

plt.show()
#