from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver
import time

def before_all(context):
    context.prepare_driver = InitWebDriver()
    context.web_driver = context.prepare_driver.init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com/")


def after_all(context):
    time.sleep(50)
    context.web_driver.quit()

"""def before_feature(context):

def before_scenario(context):
    
def before_step(context):"""