from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class google_keyword_screenshooter():

    def __init__(self, keyword, screenshot_dir, max_pages):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.keyword = keyword
        self.screenshot_dir = screenshot_dir
        self.max_pages = max_pages

    def run(self):
        self.driver.get("https://google.com")
        search_bar = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword, Keys.ENTER)
        for i in range(self.max_pages - 1):
            try:
                shitty_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "cUnQKe")))
                self.driver.execute_script("""
                const shit = arguments[0];
                shit.parentElement.removeChild(shit)
                """, shitty_element)
            except Exception:
                pass
            search_results = self.driver.find_elements(By.CLASS_NAME, "g")
            for index, search_result in enumerate(search_results):
                search_result.screenshot(
                    f"{self.screenshot_dir}/{self.keyword}x{i}x{index}.png")
            try:
                nxt_pg = self.driver.find_element(By.ID, "pnnext")
                nxt_pg.click()
            except Exception:
                pass
