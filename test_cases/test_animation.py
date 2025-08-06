from page_objects.animation_page import AnimationPage


def test_animation_page_load(landing_page):
    """Test navigation to Animation screen and verify page load success"""
    # Tap Animation menu item
    landing_page.click_animation()
    
    # Verify navigation to Animation screen and page load success
    animation_page = AnimationPage(landing_page.driver)
    assert animation_page.is_animation_page_displayed()