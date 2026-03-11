import pytest
from tests.pages.login_page import LoginPage

@pytest.mark.e2e
def test_login_success(page, base_url, credentials):
    login = LoginPage(page, base_url)
    login.goto()
    login.login(credentials["user"], credentials["pass"])
    assert page.is_visible("div#dashboard")

@pytest.mark.e2e
def test_login_fail(page, base_url):
    login = LoginPage(page, base_url)
    login.goto()
    login.login("baduser", "badpass")
    assert login.is_error_visible()
