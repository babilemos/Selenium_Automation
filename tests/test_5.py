class Test5:

    def test_signout(self, log_in):
        login_page, home_page = log_in
        home_page.click_to_signout()
        assert home_page.is_signed_out() == "Signed out", "The attempt to sign out failed"
