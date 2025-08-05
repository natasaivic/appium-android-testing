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
   pip install Appium-Python-Client
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

1. Start Appium server:
   ```bash
   appium
   ```

2. Run tests:
   ```bash
   python test_script.py
   ```

## Project Structure

```
appium-android-testing/
├── venv/                 # Virtual environment
├── ApiDemos.apk         # Test application
├── test_script.py       # Test scripts
└── README.md           # This file
```

## Capabilities

The test uses these desired capabilities:
- Platform: Android
- Device: Emulator
- App: io.appium.android.apis
- Automation: UiAutomator2

## Features Tested

- UI element interactions
- Navigation flows
- Input validation
- Screen assertions