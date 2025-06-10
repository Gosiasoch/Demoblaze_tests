from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_login(self):
        self.driver.find_element(By.ID, "login2").click()

    def click_signup(self):
        self.driver.find_element(By.ID, "signin2").click()

    def is_logout_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.ID, "logout2"))).is_displayed()
        except:
            return False