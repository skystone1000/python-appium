from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "C:\\Users\\adity\\Documents\\CSE\\Appium\\org.solovyev.android.calculator_158.apk",
    "appWaitActivity": "org.solovyev.android.calculator.wizard.WizardActivity",
    "appPackage": "org.solovyev.android.calculator"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)