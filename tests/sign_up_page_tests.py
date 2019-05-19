from fixture.pages.sign_up_page import SignUpPage
from fixture.app import App
import pytest


@pytest.fixture(scope="function")
def browser(request):
    app = App()
    request.addfinalizer(app.tearDown)
    return app.browser

def test_pass_empty_data_to_sign_up_form(browser):
    error_alert = SignUpPage(browser).\
                  open_sign_up_page()\
                  .pass_email("")\
                  .pass_passord("")\
                  .create_account()\
                  .get_error_alert()
    assert error_alert == 'E-mail cannot be empty.'

