from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        # zakładam, że przycisk „Log in” już został kliknięty
        user_input = self.wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
        pass_input = self.driver.find_element(By.ID, "loginpassword")
        user_input.clear()
        user_input.send_keys(username)
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    def accept_alert(self):
        # czekaj aż alert się pojawi, pobierz jego tekst i je zamknij
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text