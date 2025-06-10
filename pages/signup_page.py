from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "sign-username"))).send_keys(username)
        self.driver.find_element(By.ID, "sign-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    def accept_alert(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            return alert_text
        except:
            return ""