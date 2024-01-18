import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv

INSTA_ID = load_dotenv("INSTA_ID")
INSTA_SECRET = load_dotenv("INSTA_SECRET")

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(f"https://www.instagram.com/")

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aa4b")))

login_input = driver.find_elements(By.CLASS_NAME, "_aa4b")
login_btn = driver.find_element(By.CLASS_NAME, "_acap")

id_input, pw_input = login_input

id_input.send_keys(INSTA_ID)
pw_input.send_keys(INSTA_SECRET)
login_btn.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_ab6-")))

try:
    later_btn = driver.find_element(By.CLASS_NAME, "_a9_1")
    later_btn.click()
except Exception:
    pass

search_btn = driver.find_elements(By.CLASS_NAME, "_ab6-")[1]

search_btn.click()

main_hashtag = "dog"

search_bar = driver.find_element(
    By.CLASS_NAME, "x7xwk5j")

search_bar.send_keys(f"#{main_hashtag}")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".xocp1fn a")))

hashtags_list = driver.find_elements(By.CLASS_NAME, "x1cy8zhl")
hashtags_list.pop(0)

search_result = []

for hashtag in hashtags_list:
    hashtag.find_elements

time.sleep(5)
