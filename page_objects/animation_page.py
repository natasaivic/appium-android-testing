from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AnimationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Locators for Animation page elements
    PAGE_TITLE = (By.XPATH, "//android.widget.TextView[@text='API Demos']")
    BOUNCING_BALLS = (By.XPATH, "//android.widget.TextView[@text='Bouncing Balls']")
    
    def is_animation_page_displayed(self):
        """Verify if Animation page is displayed"""
        return self.is_element_visible(self.BOUNCING_BALLS)