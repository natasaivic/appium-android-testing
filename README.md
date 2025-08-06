# Appium Android Testing Project

This project demonstrates automated testing of native Android applications using Appium with Python.

## Setup

### Prerequisites
- Python 3.10+
- Node.js and npm
- Android Studio with SDK
- Java JDK

### Installation

1. Clone this repository
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Appium server and driver:
   ```bash
   npm install -g appium
   appium driver install uiautomator2
   ```

### Android Emulator Setup

1. Create an Android Virtual Device (AVD) in Android Studio
2. Start the emulator
3. Verify connection: `adb devices`

### Test Application

The project uses ApiDemos.apk for testing, which is included in the repository.

To install on emulator:
```bash
adb install ApiDemos.apk
```

## Running Tests

1. Set Android environment variables and start Appium server:
   ```bash
   ANDROID_HOME="/Users/your_username/Library/Android/sdk" ANDROID_SDK_ROOT="/Users/your_username/Library/Android/sdk" appium
   ```

2. Run tests:
   ```bash
   source venv/bin/activate
   pytest test_cases/test_accessibility.py -v
   ```

## Project Structure

```
appium-android-testing/
├── page_objects/         # Page Object Model files
│   ├── base_page.py     # Base class with reusable methods
│   ├── landing_page.py  # API Demos main screen
│   └── accessibility_page.py # Accessibility screen
├── test_cases/          # Test files
│   └── test_accessibility.py # Accessibility navigation test
├── venv/                # Virtual environment
├── ApiDemos.apk        # Test application
├── conftest.py         # Pytest configuration
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## Capabilities

The test uses these desired capabilities:
- Platform: Android
- Device: Emulator
- App: io.appium.android.apis
- Automation: UiAutomator2

## Tests Implemented

- **test_accessibility.py**: Tests navigation from main screen to Accessibility screen using Page Object Model

## Features

- Page Object Model architecture
- Automated UI navigation testing
- Pytest framework integration
- Clean project structure