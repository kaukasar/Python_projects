import time
from selenium import webdriver
from loginPage import loginPage
from environmentPage import environmentPage
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

logging.root.setLevel(logging.INFO)
log = logging.getLogger()

@pytest.fixture
def setup_teardown():
    op = Options()
    op.headless = True
    driver = webdriver.Chrome(service=Service(r'C:\Users\belva\PycharmProjects\chromedriver.exe'), options=op)
    login_page = loginPage(driver)
    environment_page = environmentPage(driver)
    driver.get('https://vdi.arbetsformedlingen.se/my.policy')
    yield login_page, environment_page
    driver.quit()

def test_login_to_test_environment(setup_teardown):
    login_page, environment_page = setup_teardown

    login_page.goto_login_page()
    login_page.enter_username('xxsfo')
    login_page.enter_password('Acctest09')
    login_page.submit_form()
    environment_page.external_test_field() #Kontrollerar att fältet finns utan att interagera med det
    environment_page.select_internal_test_environment()
    environment_page.select_html()
    environment_page.submit_form()

def test_addition():
    log.warning('Hello world')
    assert 1+1 == 2
