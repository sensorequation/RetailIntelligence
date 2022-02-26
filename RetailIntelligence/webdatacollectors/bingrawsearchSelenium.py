__author__ = 'vivek'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from bs4 import BeautifulSoup

############################## Headless Options ###########################################



############################################################################################################





def bingRawSearch(webSiteName,location = None):

    try:
        rawlinks = []
        driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
        driver.implicitly_wait(30)
        base_url = "http://www.bing.com/"
        verificationErrors = []
        accept_next_alert = True




        driver = driver
        driver.get(base_url )
        driver.find_element_by_id("sb_form_q").clear()

        if location != None:

            driver.find_element_by_id("sb_form_q").send_keys("www." + webSiteName + ".com" + " " + location)


        else:
            driver.find_element_by_id("sb_form_q").send_keys("www." + webSiteName + ".com")
        driver.find_element_by_id("sb_form_go").click()

        c = driver.page_source
        soup = BeautifulSoup(c, "html.parser")


        # print businessReviews
        for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

            tempLink = link.get('href')

            if  "http" in tempLink:

                print tempLink

                rawlinks.append(tempLink)


        time.sleep(30)

        # Go to page 2. For now we will click. Later we can implement a more dynamic feature, where href will pull in more dynamic links
        '''
        /search?q=www.chutneysmi.com&go=Submit&qs=ds&qpvt=www.chutneysmi.com
        /search?q=www.chutneysmi.com&filters=ex1%3a%22ez1%22&go=Submit&qs=ds&qpvt=www.chutneysmi.com
        /search?q=www.chutneysmi.com&filters=ex1%3a%22ez2%22&go=Submit&qs=ds&qpvt=www.chutneysmi.com
        /search?q=www.chutneysmi.com&filters=ex1%3a%22ez3%22&go=Submit&qs=ds&qpvt=www.chutneysmi.com



        '''


        driver.find_element_by_link_text("2").click()

        c = driver.page_source
        soup = BeautifulSoup(c, "html.parser")


        # print businessReviews
        for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

            tempLink = link.get('href')
            if "http" in tempLink:
                print tempLink

                rawlinks.append(tempLink)

        time.sleep(30)

        driver.find_element_by_link_text("3").click()

        c = driver.page_source
        soup = BeautifulSoup(c, "html.parser")


        # print businessReviews
        for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

            tempLink = link.get('href')
            if "http" in tempLink:
                print tempLink

                rawlinks.append(tempLink)
        time.sleep(30)


        driver.find_element_by_link_text("4").click()

        c = driver.page_source
        soup = BeautifulSoup(c, "html.parser")


        # print businessReviews
        for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

            tempLink = link.get('href')
            if "http" in tempLink:
                print tempLink

                rawlinks.append(tempLink)


        return rawlinks
    except:
        print "Exception in Bing Search"
        return rawlinks

def bingRawSearchAddresstoWebsite(address):

    rawlinks = []
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(30)
    base_url = "http://www.bing.com/"
    verificationErrors = []
    accept_next_alert = True




    driver = driver
    driver.get(base_url )
    driver.find_element_by_id("sb_form_q").clear()
    driver.find_element_by_id("sb_form_q").send_keys(address)
    driver.find_element_by_id("sb_form_go").click()

    c = driver.page_source
    soup = BeautifulSoup(c, "html.parser")


    # print businessReviews
    for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

        tempLink = link.get('href')

        if  "http" in tempLink:

            print tempLink

            rawlinks.append(tempLink)


    time.sleep(30)

    # Go to page 2. For now we will click. Later we can implement a more dynamic feature, where href will pull in more dynamic links
    '''
    /search?q=www.chutneysmi.com&go=Submit&qs=ds&qpvt=www.chutneysmi.com
    /search?q=www.chutneysmi.com&filters=ex1%3a%22ez1%22&go=Submit&qs=ds&qpvt=www.chutneysmi.com
    /search?q=www.chutneysmi.com&filters=ex1%3a%22ez2%22&go=Submit&qs=ds&qpvt=www.chutneysmi.com
    /search?q=www.chutneysmi.com&filters=ex1%3a%22ez3%22&go=Submit&qs=ds&qpvt=www.chutneysmi.com



    '''


    driver.find_element_by_link_text("2").click()

    c = driver.page_source
    soup = BeautifulSoup(c, "html.parser")


    # print businessReviews
    for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

        tempLink = link.get('href')
        if "http" in tempLink:
            print tempLink

            rawlinks.append(tempLink)

    time.sleep(30)

    driver.find_element_by_link_text("3").click()

    c = driver.page_source
    soup = BeautifulSoup(c, "html.parser")


    # print businessReviews
    for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

        tempLink = link.get('href')
        if "http" in tempLink:
            print tempLink

            rawlinks.append(tempLink)
    time.sleep(30)


    driver.find_element_by_link_text("4").click()

    c = driver.page_source
    soup = BeautifulSoup(c, "html.parser")


    # print businessReviews
    for link in soup.find_all('a', href=True):  # Find all the href which contain the business info

        tempLink = link.get('href')
        if "http" in tempLink:
            print tempLink

            rawlinks.append(tempLink)


    return rawlinks


'''
if __name__ == '__main__':
    print 'Hello, I am the scheduler'
    webSiteName = "chutneysmi"
    bingRawSearch(webSiteName)
'''