import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)


    #Locators
    select_laptops = "//a[contains(text(), 'Ноутбуки')]"
    select_macbook = "//a[contains(text(), 'Apple')]"
    select_price_slider = "//button[@class='slider__knob ng-star-inserted']"
    select_more_popular = "//span[contains(text(), 'Сначала популярные')]"
    select_more_expensive = "//div[contains(text(), 'Сначала дороже')]"
    add_to_cart_button = "//mvid-plp-cart-button//button[@class='button ng-star-inserted']"
    cart = "//p[contains(text(), 'Корзина')]"


    #Getters
    def get_select_laptops(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_laptops)))

    def get_select_macbook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_macbook)))

    def get_select_more_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_more_popular)))

    def get_select_more_expensive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_more_expensive)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))



    #Actions
    def click_select_laptops(self):
        self.get_select_laptops().click()
        print("Click select laptops")

    def click_select_macbook(self):
        self.get_select_macbook().click()
        print("Click select macbook")

    def click_select_more_popular(self):
        time.sleep(5)
        self.get_select_more_popular().click()
        print("Click select more popular macbook")

    def click_select_more_expensive(self):
        self.get_select_more_expensive().click()
        print("Click select more expensive macbook")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")
        time.sleep(5)

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")


    # Methods
    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method='select_product')
            self.click_select_laptops()
            self.click_select_macbook()
            self.click_select_more_popular()
            self.click_select_more_expensive()
            self.click_add_to_cart_button()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')




