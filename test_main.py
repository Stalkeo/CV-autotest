import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://stalkeo.github.io"

def check_url(browser, exp_links):
    for e_link in exp_links:
        url = browser.current_url
        if url == e_link[0]:
            el = browser.find_element(By.CSS_SELECTOR, value = e_link[1])
            assert el, ""
    return url


def test_open_page(browser):
  browser.get(URL)
  name = browser.find_element(By.ID, value = "name")
  assert name.text == "Даня Войтович", "Unexpected text on button"

def test_open_links(browser):
    exp_links = [
        ('https://t.me/stalkeo', '[class="tgme_page"]'),
        ('https://vk.com/stalkeo', '[class="page_name"]'), 
        ('https://volgograd.hh.ru/resume/b8fc8b5dff09d9a2f60039ed1f6d517747464c', '[class="supernova-button"]'),
        ('https://github.com/Stalkeo', '[class="vcard-names "]')
        ]
    browser.get(URL)
    links = browser.find_elements(By.TAG_NAME, 'a')
    #по тэгу "a"
    #так ты получишь коллекцию ссылок на странице
    #дальше в цикле по ним перебираешь
    for link in links:
        
        link.click()        
        url = check_url(browser=browser, exp_links=exp_links)
        
        browser.back()

        for e_link in exp_links:
            if e_link[0] == url:
                exp_links.remove(e_link) # удаляешь проверенную ссылку из списка

    assert len(exp_links) == 0, "Остались непроверенные ссылки"