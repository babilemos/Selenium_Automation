import pytest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser to run the tests')


@pytest.fixture
def choose_browser(request):
    select_browser = request.config.getoption('browser').lower()
    yield select_browser


@pytest.fixture()
def open_browser(choose_browser):
    login_page = LoginPage(browser=choose_browser)
    yield login_page
    login_page.close()


@pytest.fixture()
def log_in(open_browser):
    login_page = open_browser
    login_page.log_in()
    login_page.go_home()
    home_page = HomePage(login_page.driver)
    yield login_page, home_page
