from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_contact_modal(self):
        contact_link = self.driver.find_element(By.LINK_TEXT, "Contact")
        contact_link.click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "exampleModal")))

    def enter_email(self, email):
        email_input = self.driver.find_element(By.ID, "recipient-email")
        email_input.clear()
        email_input.send_keys(email)

    def enter_name(self, name):
        name_input = self.driver.find_element(By.ID, "recipient-name")
        name_input.clear()
        name_input.send_keys(name)

    def enter_message(self, message):
        message_input = self.driver.find_element(By.ID, "message-text")
        message_input.clear()
        message_input.send_keys(message)

    def click_send(self):
        send_button = self.driver.find_element(By.XPATH, "//button[text()='Send message']")
        send_button.click()

    def click_close(self):
        close_button = self.driver.find_element(By.XPATH, "//div[@id='exampleModal']//button[text()='Close']")
        close_button.click()

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def is_modal_closed(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.ID, "exampleModal")))
            return True
        except:
            return False