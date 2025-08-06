from page_objects.accessibility_page import AccessibilityPage


def test_accessibility_navigation(landing_page):
    """Test navigation to Accessibility screen"""
    # Tap Accessibility menu item
    landing_page.click_accessibility()
    
    # Verify navigation to Accessibility screen
    accessibility_page = AccessibilityPage(landing_page.driver)
    assert accessibility_page.is_accessibility_page_displayed()