from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from base.old_selenium_driver import SeleniumDriver
from selenium import webdriver
import logging
import utilities.custom_logger as cl
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locator
    _signin_link = "//a[@id='nav-link-accountList']"
    #_signin_button = "//span[contains(@class,'nav-action-inner')and contains(text(),'Sign in')]"
    #_signin_button = "//div[@id='nav-flyout-ya-signin']//span[contains(@class,'nav-action-inner')and contains(text(),'Sign in')]"
    _email_field = "ap_email"
    _continue_button = "continue"
    _password_field = "ap_password"
    _login_button ="signInSubmit"

    def getSignInLink(self):
        actions = ActionChains(self.driver)
        signinlink = self.driver.find_element(By.XPATH, self._signin_link)
        actions.move_to_element(signinlink).perform()
        return actions.click(signinlink)


    # def getSignInButton(self):
    #     actions = ActionChains(self.driver)
    #     signinbutton = self.driver.find_element(By.XPATH,self._signin_button)
    #     actions.move_to_element(signinbutton).perform()
    #     return actions.click(signinbutton)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getContinueButton(self):
    #     return self.driver.find_element(By.ID, self._continue_button)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)
    #
    def clickSignInLink(self):
        self.getSignInLink().perform()
        #time.sleep(3)

    # def clickSignInButton(self):
    #     time.sleep(5)
    #     self.getSignInButton().perform()
    def clearField(self,Email):
        self.elementClear(self._email_field)

    def enterEmailField(self,Email):
        self.sendKeys(Email, self._email_field,locatorType="id")

    def clickContinueButton(self):
        self.elementClick(self._continue_button,locatorType="id")

    def enterPasswordField(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="id")

    def login(self,Email=" ",password=" "):
        self.clickSignInLink()

        #self.clearFields()

        #self.clickSignInButton()
        #self.clearField(Email)

        self.enterEmailField(Email)

        self.clickContinueButton()

        self.enterPasswordField(password)

        time.sleep(3)

        self.clickLoginButton()

        
    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[@id='nav-link-accountList']/div/span[contains(text(),'Priti')]",
                                       locatorType="xpath")
        return result
    def verifyLoginFaild1(self):
        result = self.isElementPresent("//span[@class='a-list-item' and contains(text(),'We cannot find an account')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[@class='a-list-item' and contains(text(),'Your password is incorrect')]",
                                           locatorType="xpath")
        return result


        #emailField.click()

        #passwordField =self.getElement(locator=self._password_field,locatorType="id")
        #passwordField.clear()
        #emailField.click()

    def verifyLoginTitle(self):
        #return self.verifyPageTitle("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        return self.verifyPageTitle("Your Account")


    '''
    def login(self):
        baseURL = "https://www.amazon.in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(4)

        actions = ActionChains(driver)

        signinLink = driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']")
        actions.move_to_element(signinLink).perform()

        time.sleep(3)

        signinButton = driver.find_element(By.XPATH,"//span[contains(@class,'nav-action-inner')and contains(text(),'Sign in')]")
        time.sleep(2)
        actions.move_to_element(signinButton).perform()
        actions.click(signinButton).perform()

        emailField = driver.find_element(By.ID,"ap_email")
        emailField.send_keys("dk.pradhan@outlook.com")

        continueButton = driver.find_element(By.ID,"continue")
        continueButton.click()
        
        if(self.driver.find_element(By.ID,"continue")).is_displayed():

            self.driver.find_element(By.ID,"continue").click()
            passwordField = self.driver.find_element(By.ID, "ap_password")
            passwordField.send_keys(password)
        else:
            passwordField = self.driver.find_element(By.ID, "ap_password")
            passwordField.send_keys(password)
        
        
        passwordField = driver.find_element(By.ID, "ap_password")
        passwordField.send_keys("Sara@1234")

        time.sleep(4)

        loginButton = driver.find_element(By.ID,"signInSubmit")
        loginButton.click()
    '''


