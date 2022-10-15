from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from time import sleep


class CreateAccountPage(PageObject):
    id_female_radio_btn = 'id_gender2'
    id_first_name = 'customer_firstname'
    id_last_name = 'customer_lastname'
    id_password = 'passwd'
    id_date_days = 'days'
    id_day = '#days [value = "17"]'
    id_date_months = 'months'
    id_month = '#months [value = "1"]'
    id_date_years = 'years'
    id_year = '#years [value = "1987"]'
    id_offers = 'optin'
    id_address = 'address1'
    id_city = 'city'
    id_state = 'id_state'
    id_chosen_state = '#id_state [value = "32"]'
    id_zip_code = 'postcode'
    id_country = 'id_country'
    id_chosen_country = '#id_country [value = "21"]'
    id_mobile = 'phone_mobile'
    id_register_btn = 'submitAccount'
    id_account_name = 'account'

    def __init__(self, driver):
        super(CreateAccountPage, self).__init__(driver=driver)

    def fill_form(self, first_name='Antonella', last_name='Lemos Gonzaga', password='password123',
                  address='24 Waverly Pl', city='New York City', zip='10003', mobile='16468954276'):
        sleep(5)
        self.driver.find_element(By.ID, self.id_female_radio_btn).click()
        self.driver.find_element(By.ID, self.id_first_name).send_keys(first_name)
        self.driver.find_element(By.ID, self.id_last_name).send_keys(last_name)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.driver.find_element(By.ID, self.id_date_days).click()
        self.driver.find_element(By.CSS_SELECTOR, self.id_day).click()
        self.driver.find_element(By.ID, self.id_date_months).click()
        self.driver.find_element(By.CSS_SELECTOR, self.id_month).click()
        self.driver.find_element(By.ID, self.id_date_years).click()
        self.driver.find_element(By.CSS_SELECTOR, self.id_year).click()
        self.driver.find_element(By.ID, self.id_offers).click()
        self.driver.find_element(By.ID, self.id_address).send_keys(address)
        self.driver.find_element(By.ID, self.id_city).send_keys(city)
        self.driver.find_element(By.ID, self.id_state).click()
        self.driver.find_element(By.CSS_SELECTOR, self.id_chosen_state).click()
        self.driver.find_element(By.ID, self.id_zip_code).send_keys(zip)
        self.driver.find_element(By.ID, self.id_country).click()
        self.driver.find_element(By.CSS_SELECTOR, self.id_chosen_country).click()
        self.driver.find_element(By.ID, self.id_mobile).send_keys(mobile)
        self.driver.find_element(By.ID, self.id_register_btn).click()

    def is_registered(self):
        try:
            user_account = self.driver.find_element(By.CLASS_NAME, self.id_account_name).text
            return user_account
        except NoSuchElementException:
            return "Failed registration"
