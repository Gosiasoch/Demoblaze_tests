import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()

user_data = [
    (f"{fake.user_name()}{fake.random_int(1000, 9999)}", fake.password(length=10))
    for _ in range(4)
]


@pytest.mark.parametrize("username, password", user_data)
def test_register_and_login_user(home_page, signup_page, login_page, username, password):
    home_page.open()
    home_page.click_signup()
    signup_page.register(username, password)
    alert_text = signup_page.accept_alert()

    WebDriverWait(home_page.driver, 5).until_not(
        EC.visibility_of_element_located((By.ID, "signInModal"))
    )

    home_page.click_login()
    login_page.login(username, password)

    assert home_page.is_logout_visible()
