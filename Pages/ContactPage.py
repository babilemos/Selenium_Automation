from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class ContactPage(PageObject):
    url = 'http://automationpractice.com/index.php?controller=contact'
    id_price = 'our_price_display'
    id_subject = 'id_contact'
    id_chosen_subject = '#id_contact [value="2"]'
    id_chosen_subject_msg = 'desc_contact2'
    id_message = 'message'
    id_send_message_btn = 'submitMessage'
    id_sent_msg = '#center_column > p'

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver=driver)

    def is_contact_page(self):
        return self.is_page(self.url)

    def fill_contact_form(self, message='Testing contact form feature.'):
        self.driver.find_element(By.ID, self.id_subject).click()
        self.driver.find_element(By.CSS_SELECTOR, self.id_chosen_subject).click()
        self.driver.find_element(By.ID, self.id_message).send_keys(message)

    def click_to_send_message(self):
        self.driver.find_element(By.ID, self.id_send_message_btn).click()

    def verify_chosen_subject_message(self):
        return self.driver.find_element(By.ID, self.id_chosen_subject_msg).text

    def verify_sent_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.id_sent_msg).text
