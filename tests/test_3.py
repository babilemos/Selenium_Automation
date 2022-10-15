from Pages.CreateAccountPage import CreateAccountPage
from time import sleep


class Test3:

    def test_create_valid_account(self, open_browser):
        login_page = open_browser
        login_page.click_create_account_btn()
        sleep(5)
        assert login_page.check_create_account_error_message() == "Invalid email address.", "The system did not " \
                                                                  "alert about the account creation failure"
        login_page.fill_create_account_email_address(email='babi.lemos@gmail.com')
        login_page.click_create_account_btn()
        sleep(5)
        assert login_page.check_create_account_error_message() == "An account using this email address has already " \
                                                                  "been registered. Please enter a valid password or " \
                                                                  "request a new one.", "The system did not alert " \
                                                                  "about the account creation failure"
        login_page.clear_email_address_info()
        login_page.create_account()
        create_account_page = CreateAccountPage(login_page.driver)
        create_account_page.fill_form()
        assert create_account_page.is_registered() == "Antonella Lemos Gonzaga", \
            "The attempt to create a new account failed"
