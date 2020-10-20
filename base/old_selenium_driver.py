from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as cl
import time
import os

class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self,resultMessage):
        fileName = resultMessage + "." + str(round(time.time()*1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshot saved in:" + destinationFile)
        except:
            self.log.error("### Exception Occurred while taking screenshot ###")
            print_stack()


    def getTitle(self):
        return self.driver.title

    def getBytype(self,locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info(" Locatortype " + locatorType +" is not supported or correct ")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getBytype(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element is found")
        except:
            print("Element is not found")
        return element

    def elementClick(self,locator,locatorType):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info(" Click on element with locator " + locator +
                          " locator types " + locatorType )
        except:
            self.log.info(" can not click on element with locator " + locator +
                          " locator types " + locatorType)
            print_stack()

    def elementClear(self,locator,locatorType):
        try:
            element = self.getElement(locator,locatorType)
            element.clear()
            self.log.info(" Clear the element with locator " + locator +
                          " locator types " + locatorType )
        except:
            self.log.info(" can not clear the element with locator " + locator +
                          " locator types " + locatorType)
            print_stack()


    def signInLinkClick(self,locator,locatorType):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info(" Click on element with locator " + locator +
                          " locator types " + locatorType )
        except:
            self.log.info(" can not click on element with locator " + locator +
                          " locator types " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(" Sent data on element with locator " + locator +
                          " locator types " + locatorType )
        except:
            self.log.info(" can not send data on element with locator " + locator +
                          " locator types " + locatorType )
            print_stack()



    def isElementPresent(self,locator,locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            self.log.info(" Element not found ")
            return False

    def elementPresenceCheck(self,locator,byType):
        try:
            elementList = self.driver.find_elements(byType,locator)
            if len(elementList) > 0:
                print("Element is found")
                return True
            else:
                print("Element is not found")
                return False
        except:
            print("exception....")
            return False

    def waitForElement(self,locator,locatorType="id",timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.getBytype(locatorType)
            self.log.info("Waiting for maximum :: " +str(timeout)+"::seconds for element to be clickable")
            wait = WebDriverWait(self.driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(byType,"stopFilter_stops-0"))
            print("Element Appeared in the webpage ")
        except:
            print("Element not appeared in the web page")
            print_stack()
        return element




