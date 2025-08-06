from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AccessibilityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Locator for Accessibility page title
    PAGE_TITLE = (By.XPATH, "//android.widget.TextView[@text='API Demos']")
    ACCESSIBILITY_NODE_PROVIDER = (By.XPATH, "//android.widget.TextView[@text='Accessibility Node Provider']")
    
    def is_accessibility_page_displayed(self):
        """Verify if Accessibility page is displayed"""
        return self.is_element_visible(self.ACCESSIBILITY_NODE_PROVIDER)