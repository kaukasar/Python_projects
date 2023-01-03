from selenium.webdriver.common.by import By
from generalPage import generalPage
import logging
log = logging.getLogger()

class environmentPage(generalPage):
    def __init__(self, driver):
        super(environmentPage, self).__init__(driver)

    def internal_test_field(self):
        try:
            element = self.find_element(By.ID, 'remote_desktop:/TEST/vdi-acc.arbetsformedlingen.se_rd-autogen-app-2')
        except:
            raise Exception('Kunde inte hitta interna tester faltet')
        return element

    def external_test_field(self):
        try:
            element = self.find_element(By.ID, 'remote_desktop:/TEST/vdi-acc.arbetsformedlingen.se_rd-autogen-app-0')
        except:
            raise Exception('Kunde inte hitta externa tester faltet')
        return element

    def select_client_radiobutton(self):
        try:
            element = self.find_element(By.ID, 'vmware_view1')
        except:
            raise Exception('Kunde inte hitta HTML radioknappen')
        return element

    def ok_button(self):
        try:
            element = self.find_element(By.CLASS_NAME, 'apmui-button-submit')
        except:
            raise Exception('Kunde inte hitta OK knappen')
        return element

    def select_internal_test_environment(self):
        self.internal_test_field().click()
        log.info(f'Har valt Interna Tester')

    def select_html(self):
        self.select_client_radiobutton().click()
        log.info(f'Har valt oppna testmiljon i browsern')

    def submit_form(self):
        self.ok_button().click()
        log.info(f'Klickat pa ok knappen pa Select Client sidan')