import time
from selenium.webdriver.common.by import By
from utilities.Generic import Test_generic
from selenium.webdriver.common.action_chains import ActionChains

class Test_HOMEPAGE(Test_generic):
    START_FREE_TRAIL =          "//*[@id='home-page-banner']/div/a"
    TRY_FREE =                  "//*[@id='HeaderVue']/header/div[2]/div/div[2]/div/div/a"
    TOP_ELEMENT =      "//*[@id='HeaderVue']/header/div[2]/div/div[1]/a/img"
    Main_menu_options = '//*[@id="HeaderVue"]/header/div[2]/div/div[2]/div/ul'

    def Launch_the_application_and_verify_the_tittle(self):
        Tittle = self.driver.title
        assert Tittle == self.Application_Title
        self.driver.maximize_window()

    def verify_the_option_Start_Free_trial_is_visible(self):
        self.driver.find_element(By.XPATH, self.START_FREE_TRAIL).is_displayed()
        return True
        # self.is_visible(self.START_FREE_TRAIL)

    # self.is_visible(self.START_FREE_TRAIL)
    def Verify_try_free_option_is_visible(self):
        self.driver.find_element(By.XPATH, self.TRY_FREE).is_displayed()
        # self.Generic.is_visible(self.TRY_FREE)
        # self.is_visible(self.TRY_FREE)

    def verify_the_application_scrolling_feature_top_to_bottom(self):
        bottom_element = self.driver.find_element(By.LINK_TEXT, 'Customer Care')
        top_element = self.driver.find_element(By.XPATH, self.TOP_ELEMENT)
        action = ActionChains(self.driver)
        action.move_to_element(bottom_element).perform()
        time.sleep(2)
        action.move_to_element(top_element).perform()

    def verify_the_main_menu_options(self):
        options = self.driver.find_elements(By.XPATH, self.Main_menu_options)
        Element_list = []
        for element in options:
            Element_list.append(element.text)
            assert self.Expected_main_menu_options == Element_list

