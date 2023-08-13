from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=chrome_options)

browser.get("https://google.com")
search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys("hello", Keys.ENTER)

search_results = browser.find_elements(By.CLASS_NAME, "g")

for search_result in search_results:
    title = search_result.find_element(By.TAG_NAME, "h3")
    if title:
        print(title.text)

browser.quit()
