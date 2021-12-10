from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
# без выполнения скрипта js, при попытке нажатия а кнопку, будет ошибка
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# либо необходимо использовать ActionChains
_ = button.location_once_scrolled_into_view
button.click()
