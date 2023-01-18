from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    checkout_button = "//div[contains(text(), 'Перейти к оформлению')]"
    skip_button = "//div[contains(text(), 'Пропустить')]"

    #Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_skip_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.skip_button)))

    #Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    def click_skip_button(self):
        self.get_skip_button().click()
        print("Click skip button")

    # Methods
    def product_check(self):
        with allure.step("Product check"):
            Logger.add_start_step(method='product_check')
            self.click_checkout_button()
            self.click_skip_button()
            Logger.add_end_step(url=self.driver.current_url, method='product_check')






