from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Click on an element"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return True
        except TimeoutException:
            print(f"Element not clickable: {locator}")
            return False

    def send_keys(self, locator, text):
        """Send text to an element"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            print(f"Element not found for text input: {locator}")
            return False

    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        """Check if element is present in DOM"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_text(self, locator):
        """Get text from an element"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            print(f"Element not found to get text: {locator}")
            return None

    def get_attribute(self, locator, attribute_name):
        """Get attribute value from an element"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.get_attribute(attribute_name)
        except TimeoutException:
            print(f"Element not found to get attribute: {locator}")
            return None

    def wait_for_element(self, locator, timeout=10):
        """Wait for element to be present"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element not found within {timeout} seconds: {locator}")
            return None

    def scroll_to_element(self, locator):
        """Scroll to make element visible"""
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return True
        except NoSuchElementException:
            print(f"Element not found for scrolling: {locator}")
            return False

    def swipe_up(self):
        """Swipe up on the screen"""
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, 1000)

    def swipe_down(self):
        """Swipe down on the screen"""
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, 1000)

    def tap_by_coordinates(self, x, y):
        """Tap at specific coordinates"""
        self.driver.tap([(x, y)])

    def get_elements(self, locator):
        """Get multiple elements"""
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            print(f"Elements not found: {locator}")
            return []

    def is_element_clickable(self, locator, timeout=10):
        """Check if element is clickable"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False