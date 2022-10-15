from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class PaymentPage(PageObject):
    id_process_carrier_btn = 'p > button'
    id_total_price = 'total_price'
    id_pay_by_bank_wire_btn = 'bankwire'
    id_pay_by_check_btn = 'cheque'

    def __init__(self, driver):
        super(PaymentPage, self).__init__(driver=driver)

    def click_to_pay_by_bank_wire(self):
        self.driver.find_element(By.CLASS_NAME, self.id_pay_by_bank_wire_btn).click()

    def click_to_pay_by_cheque(self):
        self.driver.find_element(By.CLASS_NAME, self.id_pay_by_check_btn).click()

    def check_total_price_appears(self):
        if self.driver.find_element(By.ID, self.id_total_price):
            return True
        else:
            return False

    def get_total_price(self):
        return float(self.driver.find_element(By.ID, self.id_total_price).text.replace("$", ""))
