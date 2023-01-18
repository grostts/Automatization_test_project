import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Ordering_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    delivery_button = "//button[contains(text(), 'Доставка')]"
    delivery_address_field = "//input[@class='delivery-input-search__input delivery-input-search__input_empty']"
    approve_address ="//span[@class='delivery-search-option__text-item']"
    next_step_button = "//button[@class='payment-button mv-main-button--primary mv-main-button--medium mv-button mv-main-button ng-star-inserted']"

    #Getters
    def get_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_button)))

    def get_delivery_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_address_field)))

    def get_approve_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.approve_address)))

    def get_next_step_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_step_button)))

    #Actions
    def click_delivery_button(self):
        self.get_delivery_button().click()
        print("Click delivery button")

    def input_delivery_address(self, address):
        # self.get_delivery_address_field().click().send_keys(address)
        # self.get_delivery_address_field().click()
        self.get_delivery_address_field().send_keys(address)
        print("Input address")

    def click_approve_address(self):
        self.get_approve_address().click()
        time.sleep(1)
        print("Approve address")

    def click_next_step_button(self):
        self.get_next_step_button().click()
        print("Click next step button")


    # Methods
    def shipping_choise(self):
        with allure.step("Shipping choise"):
            Logger.add_start_step(method='shipping_choise')
            self.click_delivery_button()
            self.input_delivery_address(address="Краснодарский край, г Сочи, р-н Хостинский, Курортный пр-кт, д 37")
            self.click_approve_address()
            self.click_next_step_button()
            Logger.add_end_step(url=self.driver.current_url, method='shipping_choise')






