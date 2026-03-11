import pytest
from tests.pages.login_page import LoginPage
from tests.pages.wifi_page import WifiPage
import time

@pytest.mark.e2e
def test_change_wifi_ssid(page, base_url, credentials):
    login = LoginPage(page, base_url)
    login.goto()
    login.login(credentials["user"], credentials["pass"])

    wifi = WifiPage(page)
    wifi.open()
    new_ssid = f"prplos-test-{int(time.time())}"
    wifi.set_ssid(new_ssid)

    # verify UI shows new SSID
    assert page.input_value("input#ssid") == new_ssid
