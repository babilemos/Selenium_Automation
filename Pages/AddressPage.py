from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class AddressPage(PageObject):
    id_process_address_btn = 'p > button'

    def __init__(self, driver):
        super(AddressPage, self).__init__(driver=driver)

    def click_process_address_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_process_address_btn).click()
