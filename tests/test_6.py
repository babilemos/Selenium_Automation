from Pages.ContactPage import ContactPage


class Test6:

    def test_contact_form(self, log_in):
        login_page, home_page = log_in
        home_page.click_to_contact()
        contact_page = ContactPage(home_page.driver)
        assert contact_page.is_contact_page(), "The redirection to the contact form failed"
        contact_page.fill_contact_form()
        assert contact_page.verify_chosen_subject_message() == "For any question about a product, an order", \
            "The subject message did not appear"
        contact_page.click_to_send_message()
        assert contact_page.verify_sent_message() == "Your message has been successfully sent to our team.", \
            "The contact form message was not sent"
