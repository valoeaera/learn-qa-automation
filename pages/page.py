from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver, wait, baseurl):
        self.driver = driver
        self.wait = wait
        self.baseurl = baseurl

    def error(self, expect, actual, is_exact):
        if is_exact:
            return f"Error EXACT_MATCH_FAILED: Expected {expect}, got {actual}."
        else:
            return f"Error TEXT_NOT_PRESENT: Expected to find {expect} in {actual}."

    def click(self, *locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def find_one(self, *locator):
        return self.driver.find_element(*locator)

    def find_all(self, *locator):
        return self.driver.find_elements(*locator)

    def reload(self):
        self.driver.refresh()

    def type_into(self, text, *locator):
        text_input = self.driver.find_element(*locator)
        text_input.clear()
        text_input.send_keys(text)

    def verify_contains(self, text, *locator):
        actual = self.driver.find_element(*locator).text
        assert text in actual, self.error(text, actual, is_exact=False)

    def verify_exact(self, text, *locator):
        actual = self.driver.find_element(*locator).text
        assert text == actual, self.error(text, actual, is_exact=True)

    def verify_url(self, text):
        actual = self.driver.current_url
        assert text in actual, self.error(text, actual, is_exact=False)

    def visit(self, path):
        self.driver.get(f"{self.baseurl}{path}")

    def wait_for_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_url_change(self):
        return self.wait.until(EC.url_changes)
