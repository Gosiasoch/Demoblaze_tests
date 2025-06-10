import pytest
from faker import Faker

fake = Faker()

def test_signup_success(home_page, signup_page):
    username = fake.user_name()
    password = fake.password(length=10)
    home_page.open()
    home_page.click_signup()
    signup_page.register(username, password)
    alert_text = signup_page.accept_alert()

    assert alert_text in ("Sign up successful.", "This user already exist.")

def test_signup_existing_user(home_page, signup_page):

    home_page.open()
    home_page.click_signup()
    signup_page.register("existinguser", "password123")
    alert_text = signup_page.accept_alert()
    assert "This user already exist." in alert_text