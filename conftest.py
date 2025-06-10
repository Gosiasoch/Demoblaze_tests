import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.signup_page import SignUpPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Możesz usunąć jeśli chcesz widzieć przeglądarkę
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def signup_page(driver):
    return SignUpPage(driver)