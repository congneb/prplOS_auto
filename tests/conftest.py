import os
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv("GATEWAY_URL", "http://192.168.1.1")
ADMIN_USER = os.getenv("GATEWAY_USER", "admin")
ADMIN_PASS = os.getenv("GATEWAY_PASS", "admin")

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def credentials():
    return {"user": ADMIN_USER, "pass": ADMIN_PASS}

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    browser_name = request.config.getoption("--browser") or "chromium"
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    browser = getattr(playwright_instance, browser_name).launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser, base_url, request):
    context = browser.new_context()
    page = context.new_page()
    # auto-capture screenshot on failure
    yield page
    # teardown: keep artifacts if test failed
    if request.node.rep_call.failed:
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)
    context.close()

# hook to access test outcome in fixtures
def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:
        if call.when == "call":
            item.rep_call = call
