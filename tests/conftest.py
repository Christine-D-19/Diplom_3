import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1400,900")
        drv = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        drv = webdriver.Firefox(options=options)
        drv.set_window_size(1400, 900)

    yield drv
    drv.quit()
    