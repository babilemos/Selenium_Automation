class Test1:

    def test_unsuccessful_login(self, open_browser):
        login_page = open_browser
        login_page.click_login_btn()
        assert login_page.is_logged_in() == "Failed log in", \
            "The login attempt was successful even though email and password fields remained blank"
        assert login_page.check_error_message() == "There is 1 error\nAn email address required.", \
            "Failed login attempt error message did not appear"
        login_page.fill_email_address()
        login_page.click_login_btn()
        assert login_page.is_logged_in() == "Failed log in", \
            "The login attempt was successful even though password field remained blank"
        assert login_page.check_error_message() == "There is 1 error\nPassword is required.", \
            "Failed login attempt error message did not appear"
        login_page.wrong_login()
        assert login_page.is_logged_in() == "Failed log in", \
            "The login attempt was successful even though the credentials were wrong"
        assert login_page.check_error_message() == "There is 1 error\nInvalid email address.", \
            "Failed login attempt error message did not appear"
        login_page.clear_login_info()
        login_page.wrong_login(username='babi.lemos@gmail.com')
        assert login_page.check_error_message() == "There is 1 error\nInvalid password.", \
            "Failed login attempt error message did not appear"
