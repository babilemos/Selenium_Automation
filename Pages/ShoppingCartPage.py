from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class ShoppingCartPage(PageObject):
    url = 'http://automationpractice.com/index.php?controller=order'
    id_checkout_btn = 'checkout'
    id_proceed_to_checkout_btn = 'a.button.btn.btn-default.standard-checkout.button-medium'

    def __init__(self, driver):
        super(ShoppingCartPage, self).__init__(driver=driver)

    def is_shopping_cart_page(self):
        return self.is_page(self.url)

    def click_proceed_to_checkout_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_proceed_to_checkout_btn).click()
