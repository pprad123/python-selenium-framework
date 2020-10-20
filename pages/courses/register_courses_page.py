from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from base.old_selenium_driver import SeleniumDriver
from selenium import webdriver
import logging
import utilities.custom_logger as cl
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    _search_box = "twotabsearchtextbox"
    _seach_button = "//span[@id='nav-search-submit-text']/input[@type='submit']"
    _specified_book = "//img [contains(@class,'s-image') and contains(@alt,'Learn With Peppa')]"
    _kindle_edition = "a-autoid-2-announce"
    _addtoEbook_cart = "add-to-ebooks-cart-button"
    _proceedto_checkout = "proceed-to-checkout-btn"
    _passwd_needed = "//span[@id='auth-enter-pwd-to-cont']"


    def enterBookNameOnSearchBox(self,bookname):
        self.sendKeys(bookname,self._search_box,locatorType="id")

    def clickOnsearchButton(self):
        self.elementClick(self._seach_button,locatorType="xpath")

    def clickOnBook(self):
        self.elementClick(self._specified_book,locatorType="xpath")

    def forSwitchingWindow(self):
        self.switchToWindow(1)
        self.elementClick(self._kindle_edition,locatorType="id")


    #
    # def clickOnFormat(self):
    #     self.elementClick(self._format_check,locatorType="id")
    #
    # def clickOnKindleFormat(self):
    #     self.elementClick(self._checkfor_kindle,locatorType="xpath")
    #
    # def clickOnEdition(self):
    #     self.elementClick(self._kindle_edition,locatorType="id")
    # def forSwitchingToDefaultContent(self):
    #     self.switchToDefaultContent()

    def addToCart(self):
        self.elementClick(self._addtoEbook_cart,locatorType="id")

    def proceedToCheckout(self):
        self.elementClick(self._proceedto_checkout,locatorType="id")

    def addBookToCart(self,bookname):
        self.enterBookNameOnSearchBox(bookname)
        self.clickOnsearchButton()
        self.clickOnBook()
        self.forSwitchingWindow()
        self.addToCart()
        self.proceedToCheckout()
