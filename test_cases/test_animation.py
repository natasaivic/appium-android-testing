from page_objects.landing_page import LandingPage
from page_objects.animation_page import AnimationPage


def test_animation_page_load(driver, reset_app):
    """Test navigation to Animation screen and verify page load success"""
    # Launch app and verify landing page
    landing_page = LandingPage(driver)
    assert landing_page.is_landing_page_displayed()
    
    # Tap Animation menu item
    landing_page.click_animation()
    
    # Verify navigation to Animation screen and page load success
    animation_page = AnimationPage(driver)
    assert animation_page.is_animation_page_displayed()