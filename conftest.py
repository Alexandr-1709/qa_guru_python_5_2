from selene.support.shared import browser, config
import pytest


@pytest.fixture(scope='function')
def setup_browser():
    browser.open('https://google.com')
    browser.driver.maximize_window()
    yield browser
    browser.quit()

