from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    # Locators for main screen elements
    APP_TITLE = (By.XPATH, "//android.widget.TextView[@text='API Demos']")
    
    # Main menu items
    ACCESSIBILITY = (By.XPATH, "//android.widget.TextView[@text='Accessibility']")
    ANIMATION = (By.XPATH, "//android.widget.TextView[@text='Animation']")
    APP = (By.XPATH, "//android.widget.TextView[@text='App']")
    CONTENT = (By.XPATH, "//android.widget.TextView[@text='Content']")
    GRAPHICS = (By.XPATH, "//android.widget.TextView[@text='Graphics']")
    MEDIA = (By.XPATH, "//android.widget.TextView[@text='Media']")
    NFC = (By.XPATH, "//android.widget.TextView[@text='NFC']")
    OS = (By.XPATH, "//android.widget.TextView[@text='OS']")
    PREFERENCE = (By.XPATH, "//android.widget.TextView[@text='Preference']")
    TEXT = (By.XPATH, "//android.widget.TextView[@text='Text']")
    VIEWS = (By.XPATH, "//android.widget.TextView[@text='Views']")
    
    # Alternative locators using accessibility id or resource id if available
    MENU_LIST = (By.ID, "android:id/list")
    
    def is_landing_page_displayed(self):
        """Verify if landing page is displayed"""
        return self.is_element_visible(self.APP_TITLE, timeout=15)
    
    def get_app_title(self):
        """Get the app title text"""
        return self.get_text(self.APP_TITLE)
    
    def click_accessibility(self):
        """Click on Accessibility menu item"""
        if self.click(self.ACCESSIBILITY):
            from page_objects.accessibility_page import AccessibilityPage
            return AccessibilityPage(self.driver)
        return None
    
    def click_animation(self):
        """Click on Animation menu item"""
        if self.click(self.ANIMATION):
            from page_objects.animation_page import AnimationPage
            return AnimationPage(self.driver)
        return None
    
    def click_app(self):
        """Click on App menu item"""
        return self.click(self.APP)
    
    def click_content(self):
        """Click on Content menu item"""
        return self.click(self.CONTENT)
    
    def click_graphics(self):
        """Click on Graphics menu item"""
        return self.click(self.GRAPHICS)
    
    def click_media(self):
        """Click on Media menu item"""
        return self.click(self.MEDIA)
    
    def click_nfc(self):
        """Click on NFC menu item"""
        return self.click(self.NFC)
    
    def click_os(self):
        """Click on OS menu item"""
        return self.click(self.OS)
    
    def click_preference(self):
        """Click on Preference menu item"""
        return self.click(self.PREFERENCE)
    
    def click_text(self):
        """Click on Text menu item"""
        return self.click(self.TEXT)
    
    def click_views(self):
        """Click on Views menu item"""
        return self.click(self.VIEWS)
    
    def is_accessibility_visible(self):
        """Check if Accessibility menu item is visible"""
        return self.is_element_visible(self.ACCESSIBILITY)
    
    def is_animation_visible(self):
        """Check if Animation menu item is visible"""
        return self.is_element_visible(self.ANIMATION)
    
    def is_app_visible(self):
        """Check if App menu item is visible"""
        return self.is_element_visible(self.APP)
    
    def is_views_visible(self):
        """Check if Views menu item is visible"""
        return self.is_element_visible(self.VIEWS)
    
    def get_all_menu_items(self):
        """Get all menu items text"""
        menu_items = []
        locators = [
            self.ACCESSIBILITY, self.ANIMATION, self.APP, self.CONTENT,
            self.GRAPHICS, self.MEDIA, self.NFC, self.OS,
            self.PREFERENCE, self.TEXT, self.VIEWS
        ]
        
        for locator in locators:
            if self.is_element_visible(locator, timeout=2):
                text = self.get_text(locator)
                if text:
                    menu_items.append(text)
        
        return menu_items
    
    def scroll_to_menu_item(self, item_name):
        """Scroll to find a specific menu item"""
        locator = (By.XPATH, f"//android.widget.TextView[@text='{item_name}']")
        
        # Try to find the element first
        if self.is_element_visible(locator, timeout=2):
            return True
        
        # If not visible, scroll down to find it
        max_scrolls = 5
        for _ in range(max_scrolls):
            self.swipe_up()
            if self.is_element_visible(locator, timeout=2):
                return True
        
        return False
    
    def click_menu_item_by_text(self, item_text):
        """Click on any menu item by its text"""
        locator = (By.XPATH, f"//android.widget.TextView[@text='{item_text}']")
        
        # First try to scroll to the item
        if self.scroll_to_menu_item(item_text):
            return self.click(locator)
        
        print(f"Menu item '{item_text}' not found")
        return False