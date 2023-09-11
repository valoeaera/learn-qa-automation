from pages.home_page import HomePage


class Application:
    def __init__(self, driver, wait, baseurl):
        self.driver = driver
        self.wait = wait
        self.baseurl = baseurl

        self.home_page = HomePage(self.driver, self.wait, self.baseurl)
