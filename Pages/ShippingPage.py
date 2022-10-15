from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class ShippingPage(PageObject):
    id_process_carrier_btn = 'p > button'
    id_terms_of_service_cckbox = 'cgv'

    def __init__(self, driver):
        super(ShippingPage, self).__init__(driver=driver)

    def select_terms_of_service_checkbox(self):
        self.driver.find_element(By.ID, self.id_terms_of_service_cckbox).click()

    def click_process_carrier_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_process_carrier_btn).click()
