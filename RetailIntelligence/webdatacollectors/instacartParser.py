import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException



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
        self.dc['appPackage'] = 'com.instacart.client'
        self.dc['appActivity'] = '.browse.ICBrowseActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.switch_to.context("NATIVE_APP")
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@contentDescription='Navigation menu']").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.instacart.client:id/ic__navigation_text_name']").click()

        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@resource-id='com.instacart.client:id/ic__storechooser_view_subtitle']").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.instacart.client:id/ic__zipcode_edit_zipcode']").send_keys('48331' +"\n")
        time.sleep(5)
        #self.driver.find_element_by_xpath("//*[@resource-id='com.instacart.client:id/ic__zipcode_button_save']").click()
        #time.sleep(5)

        for x in range(0, 100):

            t = self.driver.find_elements_by_class_name("android.widget.FrameLayout")
            print t
            try:
                if self.driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='4']").get_attribute('contentDescription'):
                    print "hi"
            except NoSuchElementException:
                time.sleep(2)
                break
            try:
                if self.driver.find_element_by_xpath(
                        "//*[@class='android.widget.FrameLayout' and @index='5']").get_attribute('contentDescription'):
                    print "hi"
            except NoSuchElementException:
                time.sleep(2)
                break

            try:
                if self.driver.find_element_by_xpath(
                        "//*[@class='android.widget.FrameLayout' and @index='6']").get_attribute('contentDescription'):
                    print "hi"
            except NoSuchElementException:
                time.sleep(2)
                break

            try:
                if self.driver.find_element_by_xpath(
                        "//*[@class='android.widget.FrameLayout' and @index='4']").get_attribute('contentDescription'):
                    print "hi"
            except NoSuchElementException:
                time.sleep(2)
                break

            footNote = expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='Instacart is an independent business that is not necessarily affiliated with, endorsed or sponsored by the retailers mentioned here.']"))
            print footNote



    def getAllStoresinZip(self):
        zipList = []
        print None

    def getSamsData(self):

        print None

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
