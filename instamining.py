import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tmpinfo import insta_info

INSTAGRAM_ID = insta_info["insta_id"]
INSTAGRAM_PW = insta_info["insta_pw"]

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(f"https://www.instagram.com/")

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aa4b")))

login_input = driver.find_elements(By.CLASS_NAME, "_aa4b")
login_btn = driver.find_element(By.CLASS_NAME, "_acap")

id_input = login_input[0]
pw_input = login_input[1]

id_input.send_keys(INSTAGRAM_ID)
pw_input.send_keys(INSTAGRAM_PW)
login_btn.click()

# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "x1to3lk4")))

# driver.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_ab6-")))

search_btn = driver.find_elements(By.CLASS_NAME, "_ab6-")[1]

search_btn.click()

main_hashtag = "dog"

search_bar = driver.find_element(
    By.CLASS_NAME, "x7xwk5j")

search_bar.send_keys(f"#{main_hashtag}")

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".xocp1fn a")))

hashtags_list = driver.find_elements(By.CLASS_NAME, "x1cy8zhl")
hashtags_list.pop(0)

tmp_data = hashtags_list[3].find_element(By.TAG_NAME, "span")

print(tmp_data.text)


# time.sleep(5)
