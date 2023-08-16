import time
from math import ceil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from os import system


class responsive_tester:

    def __init__(self, urls, screenshot_dir):
        self.driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]
        self.screenshot_dir = screenshot_dir

    def screenshot(self, url):
        self.driver.get(url)
        browser_height = self.driver.get_window_size()["height"]
        system(f"mkdir {self.screenshot_dir}/{url}")
        for size in self.sizes:
            self.driver.set_window_size(size, browser_height)
            self.driver.execute_script("window.scrollTo(0,0)")
            time.sleep(3)
            scroll_size = self.driver.execute_script(
                "return document.body.scrollHeight")
            scroll_height = self.driver.execute_script(
                "return window.innerHeight")
            total_sections = ceil(scroll_size / scroll_height)
            for section in range(total_sections):
                self.driver.execute_script(
                    f"window.scrollTo(0, {(section + 1) * scroll_height})")
                self.driver.save_screenshot(
                    f"{self.screenshot_dir}/{url}/{size}x{section + 1}.png")
                time.sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshot(url)
