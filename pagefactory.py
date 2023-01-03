from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.pagefactory import PageFactory
#from seleniumpagefactory.Pagefactory import PageFactory

class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(r'C:\Users\belva\PycharmProjects\chromedriver.exe'))
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def open_page(self, url):
        super().open_page(url)

    def newsession_button(self):
        return By.LINK_TEXT, 'New session'

    def username_field(self):
        return self.driver.find_element_by_id('username')

    def password_field(self):
        return self.driver.find_element_by_id('password')

    def submit_button(self):
        return self.driver.find_element_by_class_name('apmui-button-submit')

    def goto_loginpage(self):
        self.wait.until(EC.element_to_be_clickable(self.newsession_button())).click()

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)

    def submit_form(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
