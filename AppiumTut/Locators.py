from appium import webdriver
import time
import Elements as el

desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "C:\\Users\\adity\\Documents\\CSE\\Appium\\org.solovyev.android.calculator_158.apk",
    "appWaitActivity": "org.solovyev.android.calculator.wizard.WizardActivity",
    "appPackage": "org.solovyev.android.calculator"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Skip the setup and confirm
driver.find_element_by_id(el.btnSkipId).click()
driver.find_element_by_id(el.btnYesId).click()

# ID - find_element_by_id {Id and Resource Id are same, Accessibility Id is only for ios}
# Simple Test Calculation (12 + 21 =)
driver.find_element_by_id(el.btnOneId).click()
driver.find_element_by_id(el.btnTwoId).click()
driver.find_element_by_id(el.btnPlusId).click()
driver.find_element_by_id(el.btnTwoId).click()
driver.find_element_by_id(el.btnOneId).click()
driver.find_element_by_id(el.btnEqualId).click()
time.sleep(2)

# XPATH - find_element_by_xpath - Goto History
driver.find_element_by_xpath(el.btnHistoryXpath).click()
time.sleep(2)
driver.find_element_by_xpath(el.btnHistoryBackXpath).click()
time.sleep(2)

# Send Keys - Simple Calculation
driver.find_element_by_id(el.btnClearId).click()
driver.find_element_by_id(el.calculatorEditorId).send_keys("(22-10)*10")
driver.find_element_by_id(el.btnEqualId)

# KeyCode - All Android Key codes https://developer.android.com/reference/android/view/KeyEvent
"Search Key press in search bar - Not for this app"
# driver.press_keycode(84)

# KeyCode way 2
# driver.execute_script('mobile: performEditorAction', {'action': 'search'})
"Common Actions include: go, search, send, next, done, previous"

# CLASS - Find elements by Class (Check not working)
driver.find_element_by_id(el.btnClearId).click()
driver.find_element_by_id(el.btnTwoId).click()

dotBtn = driver.find_element_by_class_name(el.btnDotClass)
# driver.set_value(dotBtn, '.')

driver.find_element_by_id(el.btnTwoId).click()