from selenium import webdriver

class InitWebDriver:

    @staticmethod
    def init_web_driver():
        web_driver = webdriver.Chrome("driver_interactions/chromedriver")
        return web_driver