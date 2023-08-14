from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

KEYWORD = "buy domain"


browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

browser.get("https://google.com")
search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys(KEYWORD, Keys.ENTER)

shitty_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cUnQKe")))

browser.execute_script("""
const shit = arguments[0];
shit.parentElement.removeChild(shit)
""", shitty_element)

search_results = browser.find_elements(By.CLASS_NAME, "g")

for index, search_result in enumerate(search_results):
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
