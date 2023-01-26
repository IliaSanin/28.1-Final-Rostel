import pytest
from selenium import webdriver


@pytest.fixture(scope='function')

def start_page():
    driver = webdriver.Chrome('/drivers/chromedriver.exe')
    # driver.maximize_window() - опционально, но не удобно)
    driver.set_window_size(1400, 1000)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    yield driver
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.quit()

