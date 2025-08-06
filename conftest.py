import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown for Appium driver"""
    
    # Desired capabilities for Android
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "io.appium.android.apis"
    options.app_activity = ".ApiDemos"
    options.automation_name = "UiAutomator2"
    options.no_reset = False
    
    # Initialize the driver
    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )
    
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function") 
def reset_app(driver):
    """Reset app to main screen before each test"""
    # With function scope driver, each test gets fresh driver
    yield