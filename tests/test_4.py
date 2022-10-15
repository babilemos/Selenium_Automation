from Pages.AddressPage import AddressPage
from Pages.ConfirmationPage import ConfirmationPage
from Pages.OrderPage import OrderPage
from Pages.PaymentPage import PaymentPage
from Pages.ShippingPage import ShippingPage
from Pages.ShoppingCartPage import ShoppingCartPage


class Test4:

    def test_complete_purchase(self, log_in):
        repeat = 3
        login_page, home_page = log_in
        total = home_page.add_random_products_to_cart(repeat=repeat)
        assert home_page.check_cart_quantity() == str(repeat), "The items were not added to the shopping cart"
        home_page.click_to_checkout()
        shoppingcart_page = ShoppingCartPage(home_page.driver)
        assert shoppingcart_page.is_shopping_cart_page(), "The redirection to the shopping cart failed"
        shoppingcart_page.click_proceed_to_checkout_btn()
        address_page = AddressPage(shoppingcart_page.driver)
        address_page.click_process_address_btn()
        shipping_page = ShippingPage(address_page.driver)
        shipping_page.select_terms_of_service_checkbox()
        shipping_page.click_process_carrier_btn()
        payment_page = PaymentPage(shipping_page.driver)
        assert payment_page.check_total_price_appears(), "The total price did not appear"
        assert payment_page.get_total_price() == total, "The total price is wrong"
        payment_page.click_to_pay_by_bank_wire()
        order_page = OrderPage(payment_page.driver)
        assert order_page.is_order_page(), "The redirection to the order page failed"
        assert order_page.check_page_subheader() == "bank-wire payment.", "The pay by bank-wire option did not work"
        order_page.click_to_confirm_order()
        confirmation_page = ConfirmationPage(order_page.driver)
        assert confirmation_page.check_page_header() == "order confirmation", "The order has not been confirmed"
        assert confirmation_page.check_order_completion() == "your order on my store is complete.", \
            "The order has not been completed"
