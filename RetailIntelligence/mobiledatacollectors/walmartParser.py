import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from imageservice import *


f = open("walmartscreendata.xml", "w")
f.close()


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '9888d9484549575832'
        self.dc['appPackage'] = 'com.walmart.grocery'
        self.dc['appActivity'] = '.screen.start.StartupActivity'
        self.dc['platformName'] = 'android'
        #self.dc['unicodeKeyboard'] = True
        #self.dc['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        #self.driver.switch_to.context("NATIVE_APP")

        time.sleep(5)
        #self.driver.find_element_by_xpath("//*[@contentDescription='Open navigation drawer']").click()
        #time.sleep(5)
        self.driver.find_element_by_xpath("//*[@contentDescription='Tap to check zip code']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='search_src_text']").send_keys('48335' + '\n')

        time.sleep(5)

        activity = self.driver.current_activity;

        if( 'FulfillmentActivity' in activity):
            self.driver.find_element_by_xpath("//*[@resource-id='com.walmart.grocery:id/radio_button']").click()
        time.sleep(5)
        # Find if the radio button is checlek, if yes then no back else back
        #self.driver.back()
        #time.sleep(5)
        #self.driver.find_element_by_xpath("//*[@text='DEPARTMENTS']").click()

        #u'.screen.fulfillment.FulfillmentActivity'
        self.driver.find_element_by_xpath("//*[@id='main_bottom_navigation_btn_departments']").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@text='Fruits & Vegetables']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@text='ORGANIC PRODUCE']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@text='FRESH FRUIT']").click()

        time.sleep(5)
        #self.driver.refresh()
        time.sleep(5)
        noOfItemsTemp = self.driver.find_element_by_xpath(
            "//*[@resource-id='com.walmart.grocery:id/text_items_count']").get_attribute('text')
        noOfItems = int(noOfItemsTemp[0])

        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@text='FRESH VEGETABLES']").click()
        time.sleep(5)
        noOfItemsTemp = self.driver.find_element_by_xpath("//*[@resource-id='com.walmart.grocery:id/text_items_count']").get_attribute('text')
        print noOfItemsTemp
        screenshotBase64 = self.driver.get_screenshot_as_base64()



        noOfItems = int(noOfItemsTemp[0])
        print "Vegetables %s" %(noOfItems)
        time.sleep(5)
        self.driver.save_screenshot(str(0) + '.png')
        time.sleep(2)

        xml_data = self.driver.page_source

        f = open("0-scrapedprices.xml", "w")
        f.write(str(xml_data))
        f.close()



        for x in range(1, 1000):

            #yoy = self.driver.find_element_by_xpath("//*[@resource-id='com.walmart.grocery:id/list_view']")

            xml_data = self.driver.page_source

            self.driver.swipe(300, 840, 300, 0, 3)

            time.sleep(4)
            screenshotBase64 = self.driver.get_screenshot_as_base64()

            self.driver.save_screenshot(str(x) + '.png')
            time.sleep(4)

            f = open( str(x) + "-scrapedprices.xml", "w")
            f.write(xml_data)
            f.close()


            imagecomparevalue = compareTwoImage(str(x-1) + '.png',str(x) + '.png')
            if imagecomparevalue == 1:
                pass
            else:
                print imagecomparevalue
                break


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
