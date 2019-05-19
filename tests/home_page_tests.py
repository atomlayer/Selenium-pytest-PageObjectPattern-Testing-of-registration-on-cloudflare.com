
from fixture.app import App
from fixture.pages.home_page import HomePage
import pytest


@pytest.fixture(scope="function")
def browser(request):
    app = App()
    request.addfinalizer(app.tearDown)
    return app.browser

def test_open_sign_up_page(browser):
    label = HomePage(browser).\
            open_home_page(). \
            click_on_signUp_link(). \
            get_value_of_started_with_cloudflare_label()
    assert "Get started with Cloudflare" == label


