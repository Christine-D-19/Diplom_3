import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def wait_for_page_ready(self, timeout: int = 15):
        end = time.time() + timeout
        while time.time() < end:
            state = self.driver.execute_script("return document.readyState")
            if state == "complete":
                return
            time.sleep(0.1)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def is_displayed(self, locator) -> bool:
        try:
            el = self.driver.find_element(*locator)
            return el.is_displayed()
        except Exception:
            return False

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception:
            self.js_click(locator)

    def js_click(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].click();", el)

    def scroll_into_view(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        return el

    def find_first_present(self, locators_list):
        last_exc = None
        for loc in locators_list:
            try:
                return self.wait.until(EC.presence_of_element_located(loc))
            except Exception as e:
                last_exc = e
        raise last_exc

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
        