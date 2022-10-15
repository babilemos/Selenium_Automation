from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class OrderPage(PageObject):
    url = 'http://automationpractice.com/index.php?fc=module&module=bankwire&controller=payment'
    id_confirm_order_btn = '#cart_navigation > button'
    id_page_subheader = 'page-subheading'

    def __init__(self, driver):
        super(OrderPage, self).__init__(driver=driver)

    def is_order_page(self):
        return self.is_page(self.url)

    def check_page_subheader(self):
        return self.driver.find_element(By.CLASS_NAME, self.id_page_subheader).text.lower()

    def click_to_confirm_order(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_confirm_order_btn).click()
