import allure

from base.base_class import Base
from utilities.logger import Logger


class Init_page(Base):
    url = 'https://www.mvideo.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    #Getters


    #Actions


    # Methods
    def initial(self):
        with allure.step("Initial"):
            Logger.add_start_step(method='initial')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='initial')



