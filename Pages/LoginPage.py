from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
import random
import string


class LoginPage(PageObject):
    url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    id_signin_btn = 'login'
    id_login_btn = 'SubmitLogin'
    id_create_account_btn = 'SubmitCreate'
    id_home_btn = '.btn.btn-default.button.button-small[title="Home"]'
    id_error_msg = '#center_column > div.alert.alert-danger'
    id_error_msg_account_creation = 'create_account_error'
    id_account_name = 'account'
    id_username = 'email'
    id_password = 'passwd'
    id_email = 'email_create'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.open_page()

    def open_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def click_create_account_btn(self):
        self.driver.find_element(By.ID, self.id_create_account_btn).click()

    def fill_email_address(self, username='idonotexist@email.com'):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)

    def fill_create_account_email_address(self, email='idonotexist@email.com'):
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def check_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.id_error_msg).text

    def check_create_account_error_message(self):
        return self.driver.find_element(By.ID, self.id_error_msg_account_creation).text

    def clear_login_info(self):
        self.driver.find_element(By.ID, self.id_username).clear()
        self.driver.find_element(By.ID, self.id_password).clear()

    def clear_email_address_info(self):
        self.driver.find_element(By.ID, self.id_email).clear()

    def wrong_login(self, username='idonotexist@email.com', password='123'):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()

    def is_login_url(self):
        return self.is_page(self.url)

    def log_in(self, username='babi.lemos@gmail.com', password='teste123'):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()

    def is_logged_in(self):
        try:
            user_account = self.driver.find_element(By.CLASS_NAME, self.id_account_name).text
            return user_account
        except NoSuchElementException:
            return "Failed log in"

    def create_account(self):
        letters = string.ascii_lowercase
        prefix = ''.join(random.choice(letters) for i in range(8))
        email = prefix + "@email.com"
        self.driver.find_element(By.ID, self.id_email).send_keys(email)
        self.click_create_account_btn()

    def go_home(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_home_btn).click()
