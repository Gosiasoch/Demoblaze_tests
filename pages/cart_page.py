from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_cart(self):
        self.driver.find_element(By.ID, "cartur").click()

    def click_place_order(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()

    def place_order(self,
                    name="Test User",
                    country="Test Country",
                    city="Test City",
                    card="1234567890123456",
                    month="12",
                    year="2030"):

        self.click_place_order()

        self.wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)
        self.driver.find_element(By.XPATH, "//button[text()='Purchase']").click()


        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert")))
            return True
        except:
            return False

    def delete_product(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Delete']").click()
