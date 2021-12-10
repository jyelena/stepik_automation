from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    browser.execute_script("window.scrollBy(0, 200);")
    result = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split(': ')[-1])

finally:
    time.sleep(10)
    browser.quit()
