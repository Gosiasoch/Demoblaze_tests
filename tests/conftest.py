import pytest
import sys
import os
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.home_page import HomePage
from pages.signup_page import SignUpPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.contact_page import ContactPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.demoblaze.com/")
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def signup_page(driver):
    return SignUpPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def contact_page(driver):
    return ContactPage(driver)
