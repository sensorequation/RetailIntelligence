__author__ = 'vivek'
import urllib2
from bs4 import BeautifulSoup

#helloworld = "<p>Hello World</p>"
#soup_string = BeautifulSoup()
#print soup_string

url = "http://www.i20fever.com/Universitybystate.html"
page = urllib2.urlopen(url)
#soup_packtpage = BeautifulSoup(page)

soup_url = BeautifulSoup(page)
print(soup_url)
