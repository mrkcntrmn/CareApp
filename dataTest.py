'''
Created on Feb 15, 2017

@author: MARK
'''
import csv
with open('ChildCareCenters.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
# [['This is the first line', 'Line1'],
#  ['This is the second line', 'Line2'],
#  ['This is the third line', 'Line3']]