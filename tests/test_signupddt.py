import pytest
from faker import Faker

fake = Faker()

test_data = [(fake.user_name(), fake.password(length=10)) for _ in range(4)]

@pytest.mark.parametrize("username, password", test_data)
def test_signup_multiple_users(home_page, signup_page, username, password):
    home_page.open()
    home_page.click_signup()
    signup_page.register(username, password)
    alert_text = signup_page.accept_alert()
    assert "Sign up successful." in alert_text or "This user already exist." in alert_text