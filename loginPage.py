from selenium.webdriver.common.by import By
from generalPage import generalPage
import logging
log = logging.getLogger()

class loginPage(generalPage):
    def __init__(self, driver):
        super(loginPage, self).__init__(driver)

    def newsession_field(self):
        try:
            element = self.find_element(By.LINK_TEXT, 'New session')
        except:
            raise Exception('Kunde inte hitta "new session" faltet')
        return element

    def username_field(self):
        try:
            element = self.find_element(By.ID, 'username')
        except:
            raise Exception('Kunde inte hitta "username" faltet')
        return element

    def password_field(self):
        try:
            element = self.find_element(By.ID, 'password')
        except:
            raise Exception('Kunde inte hitta "password" faltet')
        return element

    def submit_button(self):
        try:
            element = self.find_element(By.CLASS_NAME, 'apmui-button-submit')
        except:
            raise Exception('Kunde inte hitta "submit" knappen')
        return element

    def goto_login_page(self):
        self.newsession_field().click()
        log.info(f'Laddat inloggningssidan')

    def enter_username(self, usr):
        self.username_field().send_keys(usr)
        log.info(f'Angav {usr} i username faltet')

    def enter_password(self, pwd):
        self.password_field().send_keys(pwd)
        log.info(f'Angav {pwd} i password faltet')

    def submit_form(self):
        self.submit_button().click()
        log.info(f'Klickat pa submit knappen pa inloggningssidan')