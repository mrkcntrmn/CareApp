#import the library used to query a website

import urllib2
#print "library urllib2 imported"

#specify the url
website = "https://www.dfps.state.tx.us/Child_Care/Search_Texas_Child_Care/CCLNET/Source/Provider/ppComplianceHistory.aspx?fid=773628&tab=2"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(website)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "lxml")

right_table = soup.find('table', class_='dxgvControl_Glass')

print right_table



#for link in soup.find_all('a')
#    print(link.get('href'))

