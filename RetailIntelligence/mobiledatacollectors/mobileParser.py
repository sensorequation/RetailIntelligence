import unittest
import time
from appium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction

scrapedInfo = []

f = open("scrapedprices.txt", "w")
f.close()


#from uiautomator import device as d

itemList = ['tomatoes','bell peppers', 'spinach', 'tomatillo','eggplant','lettuce','banana','apple']
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
        #9888d9484549575832
        self.dc['udid'] = '9888d9484549575832'
        #self.dc['udid'] = 'emulator-5554'
        self.dc['appPackage'] = 'com.kroger.mobile'
        self.dc['appActivity'] = '.BannerSelectionActivity'
        self.dc['platformName'] = 'android'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub' ,self.dc)

    def instaCart(self):

        print None

    def meijer(self):
        print None

    def walmart(self):
        print None

    def buschs(self):
        print None

    def freshco(self):
        print None


    def testUntitled(self):
        time.sleep(5)
        #elem = self.driver.find_element_by_class_name('android.widget.EditText')
        #print elem ////*[@contentDescription='Open Navigation']
        self.driver.find_element_by_xpath("//*[@contentDescription='Open Navigation']").click()
        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@text= 'Stores']").click()

        time.sleep(5)
        # Click on Store and Enter ZipCode

        self.driver.find_element_by_xpath("//*[@id='menu_search']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='menu_search']").send_keys("48335" +"\n")
        time.sleep(15)

        # Click the first item in the list

        #//*[@id='storeTypeIcon' and @height>0 and ./following-sibling::*[./*[./*[./*[@text='Halstead Village Kroger']]]]]
        # //*[@id='storeTypeIcon' and @height>0 and ./parent::*[./parent::*[@contentDescription='Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy is Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy phone number (248) 489-8054']]]
        # //*[@index='0']
        # //*[@class='android.widget.LinearLayout' and @height>0 and ./*[./*[./*[./*[@text='Halstead Village Kroger']]]] and ./*[@id='storeTypeIcon']]
        # //*[@id='stores_list_recycler_view']

        #t = self.driver.find_element_by_xpath("//*[@id='stores_list_recycler_view']")
        #time.sleep(3)

        #//*[@id='stores_list_view']
        #b = self.driver.find_element_by_xpath("//*[@id='stores_list_view']")
        #time.sleep(3)
        # //*[@contentDescription='Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy is Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy phone number (248) 489-8054']
        #List
        #profile = self.driver.findElements(By.xpath("//android.view.ViewGroup 0"))
        #time.sleep(3)

        # //*[@class='android.widget.LinearLayout']

        #p = self.driver.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup']")
        #p = self.driver.find_elements_by_class_name("//*[@class='android.view.ViewGroup[0]']")
        #time.sleep(3)

        #p1 = self.driver.find_elements_by_class_name("//*[@class='android.support.v7.widget.RecyclerView']")
        #time.sleep(3)

        #p2 = p1.driver.find_element_by_xpath("//*[@id='stores_list_recycler_view']")
        #time.sleep(3)

        #WebElement plist = wd.findElement(By.xpath("//android.support.v7.widget.RecyclerView[contains(@resources-id,'id/patient_list_view') and @index='6']"));

        #plist = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[contains(@resource-id='com.kroger.mobile:id/stores_list_recycler_view' and @index='0')]")
        #time.sleep(3)
        #header =  self.driver.find_element_by_xpath("//*[@id='stores_list_view']")
        #time.sleep(3)

        #p2 = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/stores_list_recycler_view']")
        #time.sleep(3)
        p3 = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/stores_list_recycler_view' and @index='0']")
        time.sleep(3)
        p3 = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/stores_list_recycler_view' and @index='0']").click()
        time.sleep(3)

        makePReferredStore = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/quick_view_preferred_store_text' and @index='1']").click()
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[ @ contentDescription = 'Collapse']").click()
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@contentDescription='Open Navigation']").click()
        time.sleep(5)

        for i in itemList:

            self.driver.find_element_by_xpath("//*[@text = 'Home']").click()
            time.sleep(5)

            # ##### now search for the product ##############################
            self.driver.find_element_by_xpath("//*[@text='Search Items']").send_keys(i + "\n")
            time.sleep(5)

            '''
            topItem = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/product_view_cell' and @index='0'")
            time.sleep(3)
    
            bottomItem = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/product_view_cell' and @index='2'")
            time.sleep(3)
            '''
            # //*[@resource-id='com.kroger.mobile:id/item_name']

            time.sleep(3)
            #//*[@id='text1']
            totalProductstemp = self.driver.find_element_by_xpath("//*[@id = 'text1']").get_attribute('text')
            print totalProductstemp

            totalProducts = totalProductstemp.split()

            totalProductstemp = self.driver.find_element_by_xpath("//*[@class='android.widget.TextView']").get_attribute('text')
            print totalProductstemp

            #self.driver.find_element_by_xpath("//*[@id='filterItems']").click()

            #time.sleep(3)
            #self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/filter_checkbox']").click()
            #self.driver.find_element_by_xpath("//[@content-desc='*.Produce.*']")
            #//*[@text='Produce (24)']
            #time.sleep(3)
            #self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/filter_apply_button']").click()
            #time.sleep(3)
            '''
            #itemlist11 = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/product_view_cell' and @index='0']").get_property('contentDescription')
            item1 = self.driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout' and @index='0']").get_attribute('contentDescription')

            #el = self.driver.find_element_by_accessibility_id(item1)
            scrollitem1 =  self.driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout' and @index='0']")
            yCoordinate1 =  self.driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout' and @index='0']").get_attribute('y')

            print item1
            item2 = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.RelativeLayout' and @index='1']").get_attribute('contentDescription')
            scrollitem2 =  self.driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout' and @index='1']")
            yCoordinate2 = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.RelativeLayout' and @index='1']").get_attribute('y')

            print item2

            item3 = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.RelativeLayout' and @index='2']").get_attribute('contentDescription')
            #els = self.driver.find_element_by_accessibility_id(item3)
            scrollitem3 = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.RelativeLayout' and @index='2']")
            yCoordinate3 = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.RelativeLayout' and @index='2']").get_attribute('y')

            print item3

            '''

            '''
            actions = TouchAction(self.driver)
            actions.scroll_from_element(element, 10, 100)
            actions.scroll(10, 100)
            actions.perform()
            '''

            time.sleep(3)

            '''
            actions = TouchAction(self.driver)
            actions.move_to(el=None, x=None, y = 1000)
            actions.perform()

            time.sleep(3)
            '''

            #self.driver.execute_script("mobile: scroll", {"direction": "down"})


            
            #list = self.driver.find_element_by_id('com.kroger.mobile:id/product_view_cell')
            ###list = self.driver.find_element_by_accessibility_id(item3)
            #list = self.driver.find_element_by_id(el)

            # define touch
            action = TouchAction(self.driver)

            # adjust here to your needs !


            for x in range(0,int(totalProducts[0])):
                #action.press(x=50,y=200).move_to(x=50, y=-200).release().perform()


                # itemlist11 = self.driver.find_element_by_xpath("//*[@resource-id='com.kroger.mobile:id/product_view_cell' and @index='0']").get_property('contentDescription')
                item1 = self.driver.find_element_by_xpath(
                    "//*[@class='android.widget.RelativeLayout' and @index='0']").get_attribute('contentDescription')

                scrapedInfo.append(item1)
                print item1
                item2 = self.driver.find_element_by_xpath(
                    "//*[@class='android.widget.RelativeLayout' and @index='1']").get_attribute('contentDescription')

                scrapedInfo.append(item2)
                print item2

                item3 = self.driver.find_element_by_xpath(
                    "//*[@class='android.widget.RelativeLayout' and @index='2']").get_attribute('contentDescription')

                scrapedInfo.append(item3)
                print item3

                #self.driver.drag_and_drop(el,els)
                #self.driver.scroll(el,els)
                #self.driver.swipe(0,0,0,600,0)
                self.driver.swipe(300, 840, 300, 0, 3)
                #self.driver.swipe(0, 300, 0, 400, 3)
                #self.driver.swipe(0, 300, 0, 400, 3)

                #self.driver.swipe()

                #action.press(el).moveTo(els).release().perform()

                #action.scroll_from_element(list, 10, 100)
                #action.scroll(10, 100)
                #action.perform()
                time.sleep(1)

            # Add to clean up the data
            print list(set(scrapedInfo))
            f = open("scrapedprices.txt", "a")
            f.write(str(list(set(scrapedInfo))))
            f.close()
            self.driver.back()


            '''
            
            q = self.driver.find_elements_by_class_name("//*[@class='android.support.v7.widget.RecyclerView']")
            time.sleep(3)
    
            r =  self.driver.find_element_by_xpath("//*[@id='stores_list_view']")'
            time.sleep(3)
    
    
    
            #//*[@contentDescription='Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy is Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy phone number (248) 489-8054']
    
            temp1 = self.driver.find_element_by_xpath("//*[@contentDescription='Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy is Halstead Village Halstead Village 1.90 miles. phone number (248) 489-3170. store is OPEN until 12:00 am. pharmacy phone number (248) 489-8054']")
            time.sleep(3)
    
            #//*[@class='android.widget.LinearLayout' and @height>0 and ./*[./*[./*[./*[@text='Halstead Village Kroger']]]] and ./*[@id='storeTypeIcon']]
    
            temp2 = self.driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @height>0 and ./*[./*[./*[./*[@text='Halstead Village Kroger']]]] and ./*[@id='storeTypeIcon']]")
            time.sleep(3)
            #//*[@id='storeTypeIcon' and @height>0 and ./following-sibling::*[./*[./*[./*[@text='Halstead Village Kroger']]]]]
    
            temp3 = self.driver.find_element_by_xpath("//*[@id='storeTypeIcon' and @height>0 and ./following-sibling::*[./*[./*[./*[@text='Halstead Village Kroger']]]]]")
            time.sleep(3)
            #//*[@class='android.view.ViewGroup' and @height>0 and ./*[@id='name_address' and ./*[./*[@text='Halstead Village Kroger']]]]
    
            temp4 = self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and @height>0 and ./*[@id='name_address' and ./*[./*[@text='Halstead Village Kroger']]]]")
            time.sleep(3)
    
            #//*[@id='name_address' and @height>0 and ./*[./*[@text='Halstead Village Kroger']]]
    
            temp5 = self.driver.find_element_by_xpath("//*[@id='name_address' and @height>0 and ./*[./*[@text='Halstead Village Kroger']]]")
            time.sleep(3)
    
    
            #//*[@id='linearLayout2' and @height>0 and ./*[@text='Halstead Village Kroger']]
    
            temp6 = self.driver.find_element_by_xpath("//*[@id='linearLayout2' and @height>0 and ./*[@text='Halstead Village Kroger']]")
            time.sleep(3)
    
            #//*[@text='Halstead Village Kroger']
    
            temp7 = self.driver.find_element_by_xpath("//*[@text='Halstead Village Kroger']")
            time.sleep(3)
            '''

    def tearDown(self):
        self.driver.quit()
'''
    if __name__ == '__main__':
        unittest.main()
'''