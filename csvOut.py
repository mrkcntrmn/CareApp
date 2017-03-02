'''
Created on Feb 15, 2017

@author: MARK
'''
import csv
with open('ChildCareCenters.csv', 'r') as file:
    reader = csv.reader(file)
    centers_list = list(reader)

with open('ChildCareCentersEdited.csv', 'wb') as newFile:
    writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerows(centers_list)

with open('ChildCareCentersEdited.csv', 'r') as testFile:
    newReader = csv.reader(testFile)
    test_list = list(newReader)



print(test_list[0])
print(test_list[2923])
