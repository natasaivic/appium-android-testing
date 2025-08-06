from page_objects.landing_page import LandingPage
from page_objects.accessibility_page import AccessibilityPage


def test_accessibility_navigation(driver, reset_app):
    """Test navigation to Accessibility screen"""
    # Launch app and verify landing page
    landing_page = LandingPage(driver)
    assert landing_page.is_landing_page_displayed()
    
    # Tap Accessibility menu item
    landing_page.click_accessibility()
    
    # Verify navigation to Accessibility screen
    accessibility_page = AccessibilityPage(driver)
    assert accessibility_page.is_accessibility_page_displayed()