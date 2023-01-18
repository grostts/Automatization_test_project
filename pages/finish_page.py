import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators


    #Getters


    #Actions


    # Methods
    def finish(self):
        with allure.step("Finish"):
            time.sleep(5)
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.get_screenshot()
            self.assert_url('https://www.mvideo.ru/purchase/step2')
            Logger.add_end_step(url=self.driver.current_url, method='finish')




