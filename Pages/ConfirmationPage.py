from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class ConfirmationPage(PageObject):
    id_confirm_order_btn = '#cart_navigation > button'
    id_page_header = 'page-heading'
    id_order_complete = 'cheque-indent'

    def __init__(self, driver):
        super(ConfirmationPage, self).__init__(driver=driver)

    def check_page_header(self):
        return self.driver.find_element(By.CLASS_NAME, self.id_page_header).text.lower()

    def check_order_completion(self):
        return self.driver.find_element(By.CLASS_NAME, self.id_order_complete).text.lower()
