from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_signup_button(self):
        signup_button = self.driver.find_element(By.ID, "signin2")
        signup_button.click()