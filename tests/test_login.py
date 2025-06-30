import pytest
from faker import Faker

fake = Faker()

def test_login_success(home_page, login_page):
    home_page.open()
    home_page.click_login()
    login_page.login("tropic", "X9%LGw")
    assert home_page.is_logout_visible()

def test_login_wrong_username(home_page, login_page):
    home_page.open()
    home_page.click_login()
    username = fake.user_name()
    password = fake.password(length=10)
    login_page.login(username, password)

    assert not home_page.is_logout_visible()

def test_login_empty_fields(home_page, login_page):
    home_page.open()
    home_page.click_login()
    login_page.login("", "")
    alert_text = login_page.accept_alert()
    assert "Please fill out Username and Password." in alert_text