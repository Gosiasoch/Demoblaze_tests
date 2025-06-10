from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_first_product(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hrefch"))).click()

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))).click()

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text