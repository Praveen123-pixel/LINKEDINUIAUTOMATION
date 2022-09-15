import time

from selenium.webdriver.common.by import By
from utilities.Generic import Test_generic
from selenium.webdriver.common.action_chains import ActionChains
import logging
logging.basicConfig(level=logging.DEBUG)
class Login_page(Test_generic):

    generic = Test_generic()
    USER_NAME = (By.XPATH,"//*[@id='username']")
    PASS_WORD = (By.XPATH,"//*[@id='password']")
    SIGN_IN  = (By.XPATH,"//*[@id='organic-div']/form/div[3]/button")
    HOME_PAGE_TITLE =(By.XPATH,"//*[@id='global-nav-typeahead']/input")
    LOGIN_BOX = (By.XPATH,"//*[@id='app__container']/main/div[2]")



    def enter_the_username_on_username_place_holder(self,user_name):
        self.generic.do_send_key(self.USER_NAME,user_name)
        logging.info("User name entered sucessfully")

    def enter_the_password_on_password_place_holder(self,password):
        self.generic.do_send_key(self.PASS_WORD,password)

    def verify_the_home_page_of_application(self):
        try:
          self.generic.is_visible(self.HOME_PAGE_TITLE)
          #home_page_title = self.generic.get_element_text(self.HOME_PAGE_TITLE)
          logging.info("!!!!!!!!!!!!Home page verified !!!!!!!")
        except:
            self.is_visible(self.LOGIN_BOX)
            logging.info("!!!!!!!!!",self.get_element_text(self.LOGIN_BOX))



    def click_on_sign_in_button(self):
        try:
         self.generic.do_click(self.SIGN_IN)
         self.verify_the_home_page_of_application()
        except:
          logging.error("!!!!!!!!!!!!Please ENTER RIGHT CREDENTAIL")

    def verify_the_app_is_scrolling_top_to_bottom_to_top(self):
        self.generic.verify_scrolling_feature()






