import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.initial_page import Init_page
from pages.main_page import Main_page
from pages.ordering_page import Ordering_page


@allure.description("Test buy product")
def test_buy_product(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    s = Service('C:\\Users\\hp\\PycharmProjects\\Software Testing Automation and Programming.Python.Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)

    print('Start Test')

    init = Init_page(driver)
    init.initial()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.product_check()

    op = Ordering_page(driver)
    op.shipping_choise()

    fn = Finish_page(driver)
    fn.finish()

    driver.quit()







