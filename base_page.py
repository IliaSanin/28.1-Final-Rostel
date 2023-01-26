from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver, url, timeout=60):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname