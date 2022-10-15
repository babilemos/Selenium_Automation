from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from time import sleep
from random import randint


class HomePage(PageObject):
    url = 'http://automationpractice.com/index.php'
    id_price = 'our_price_display'
    id_add_to_cart_btn = '//*[@id="add_to_cart"]/button'
    id_continue_shopping_btn = 'div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > span'
    id_cart_quantity = 'span.ajax_cart_quantity'
    id_cart_btn = '[title="View my shopping cart"]'
    id_signout_btn = 'div:nth-child(2) > a'
    id_contact_us_btn = 'contact-link'
    id_account_name = 'account'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver=driver)

    def is_home_page(self):
        return self.is_page(self.url)

    def add_random_products_to_cart(self, repeat=1):
        total = 2
        for _ in range(repeat):
            random_number = randint(1, 7)
            id_random_product = "//*[@id='homefeatured']/li[" + str(random_number) + "]/div/div[2]/h5/a"
            self.driver.find_element(By.XPATH, id_random_product).click()
            sleep(5)
            total += float(self.driver.find_element(By.ID, self.id_price).text.replace("$", ""))
            self.driver.find_element(By.XPATH, self.id_add_to_cart_btn).click()
            sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, self.id_continue_shopping_btn).click()
            self.go_back_to_previous_page()
            self.refresh_page()
        return total

    def check_cart_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.id_cart_quantity).text

    def click_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_cart_btn).click()

    def click_to_signout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_signout_btn).click()

    def is_signed_out(self):
        try:
            user_account = self.driver.find_element(By.CLASS_NAME, self.id_account_name).text
            return user_account
        except NoSuchElementException:
            return "Signed out"

    def click_to_contact(self):
        self.driver.find_element(By.ID, self.id_contact_us_btn).click()
