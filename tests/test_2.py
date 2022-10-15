from Pages.HomePage import HomePage


class Test2:

    def test_successful_login(self, open_browser):
        login_page = open_browser
        login_page.log_in()
        assert login_page.is_logged_in() == "Bárbara Borba Lemos", \
            "The login attempt was unsuccessful! even though the credentials were right"
        login_page.go_home()
        home_page = HomePage(login_page.driver)
        assert home_page.is_home_page(), "The home page did not load"
        assert login_page.is_logged_in() == "Bárbara Borba Lemos", \
            "The system logged the user out when navigating to the home page from the login page"
