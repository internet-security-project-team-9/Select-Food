import time
from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

OPTIONS = Options()
OPTIONS.add_argument('--headless')
OPTIONS.add_argument('--window-size=1920x1080')
OPTIONS.add_argument("--disable-gpu")
OPTIONS.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
SERVICE = Service(executable_path="/usr/bin/chromedriver")
DRIVER = webdriver.Chrome(service=SERVICE, options=OPTIONS)

URL = 'https://map.naver.com/v5/search/'

KEY_WORD = '스시'

DRIVER.get(URL + KEY_WORD)

DRIVER.implicitly_wait(10)
try:
    DRIVER.switch_to.frame(DRIVER.find_element(By.XPATH, '//*[@id="entryIframe"]'))
except NoSuchElementException:
    DRIVER.switch_to.frame(DRIVER.find_element(By.XPATH, '//*[@id="searchIframe"]'))

    DRIVER.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container > ul > li:nth-child(1)").click()
    DRIVER.find_element(By.TAG_NAME, "a").click()

    DRIVER.switch_to.default_content()
    DRIVER.switch_to.frame(DRIVER.find_element(By.XPATH, '//*[@id="entryIframe"]'))

# with open("/home/teamuser/searchResult.txt", 'w') as f:
#     f.write(BeautifulSoup(DRIVER.page_source, "html.parser").prettify())

#TABS = DRIVER.find_elements(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a')
TABS = DRIVER.find_elements(By.CSS_SELECTOR, 'div.place_fixed_maintab > div > div > div > div > a')

for tab in TABS:
    cursor = tab.find_element(By.TAG_NAME, 'span').get_attribute("innerHTML")
    if (cursor == "메뉴"):
          tab.click()
          break

#ELEMENTSET = DRIVER.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[6]/div[2]/div[1]/div/ul')

#여기에서 메뉴가 주문 창으로 넘어가면 빧어버림
ELEMENTSET = DRIVER.find_element(By.CSS_SELECTOR, '.place_section_content').find_elements(By.TAG_NAME, "li")

# print(BeautifulSoup(DRIVER.find_element(By.CSS_SELECTOR, '.place_section_content').get_attribute("innerHTML"), "html.parser").prettify())

# for element in ELEMENTSET:
#     print(BeautifulSoup(element.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"), "html.parser").prettify())

# input()

ELEMENTS = DRIVER.find_element(By.CSS_SELECTOR, '.place_section_content').find_elements(By.TAG_NAME, "span")

for values in ELEMENTS:
        print(BeautifulSoup(values.get_attribute("innerHTML"), "html.parser").prettify())