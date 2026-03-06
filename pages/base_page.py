from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_url_contains(self, value: str):
        return self.wait.until(EC.url_contains(value))

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        return element

    def set_text(self, locator, value: str):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    def get_texts(self, locator):
        return [element.text.strip() for element in self.find_elements(locator)]

    def wait_text_in_element(self, locator, value: str):
        return self.wait.until(EC.text_to_be_present_in_element(locator, value))

    def html5_drag_and_drop(self, source, target):
        js = """
        const src = arguments[0];
        const tgt = arguments[1];
        const dataTransfer = new DataTransfer();

        function fire(type, elem, dt) {
            const evt = new DragEvent(type, {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            elem.dispatchEvent(evt);
        }

        fire('dragstart', src, dataTransfer);
        fire('dragenter', tgt, dataTransfer);
        fire('dragover', tgt, dataTransfer);
        fire('drop', tgt, dataTransfer);
        fire('dragend', src, dataTransfer);
        """
        self.driver.execute_script(js, source, target)

    def drag_and_drop(self, source_locator, target_locator):
        source = self.scroll_into_view(source_locator)
        target = self.scroll_into_view(target_locator)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except TimeoutException:
            self.html5_drag_and_drop(source, target)
            