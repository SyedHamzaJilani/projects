import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


def perform_search(driver, website_link, search_box_xpath, search):
    """Opens a webpage in the browser and perform search
    Format: perform_search(driver, "website link", "search box's XPATH", "Search")"""
    driver.get(website_link)
    search_box = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, search_box_xpath))
    )
    search_box.send_keys(search)
    search_box.send_keys(Keys.RETURN)


def click_on(driver, link_xpath):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, link_xpath))
    ).click()


def save_data(driver, data_xpath, file_name="Selenium_File", folder_path=None):
    """Default folder with the name 'Selenium Projects' will be created if no folder path is provided
       Default file name is Selenium_File
       Format: save_data(driver, "data's xpath", "file name", "folder path")"""

    store_data = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, data_xpath))
    ).text
    if folder_path is None:
        folder_path = Path.home() / "Desktop" / "Python_Selenium_Sample"
        folder_path.mkdir(parents=True, exist_ok=True)
    if folder_path is not None:
        Path(folder_path).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(folder_path, f"{file_name}.txt")
    with open(file_path, "w") as file:
        file.write(store_data)
    print(f"The file has been successfully saved in {folder_path} with the name {file_name}")


web_driver = webdriver.Chrome()


perform_search(web_driver,
               "https://www.google.com",
               "//textarea[@name='q']",
               "What is Python?")

click_on(web_driver,
         "//h3[contains(text(),'Python (programming language)')]")

save_data(web_driver,
          "//body[1]/div[2]/div[1]/div[3]/main[1]/div[3]/div[3]/div[1]/p[2]",
          "Python_Wiki")


time.sleep(20)

