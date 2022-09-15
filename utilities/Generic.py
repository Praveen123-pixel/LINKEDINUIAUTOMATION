import time

from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Test_generic():

    url ="https://www.linkedin.com/login"
    driver = webdriver.Chrome()

    def do_click(self, By_locater):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).click()
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By_locater)).click()

    def do_send_key(self, By_locater, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).send_keys(text)

    def get_element_text(self, By_locater):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(By_locater)).text
        return element

    def is_visible(self, By_locater):
        element = WebDriverWait(self.driver,5).until(EC.visibility_of_any_elements_located(By_locater))
        return bool(element)

    def select_the_element(self, By_locater):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).click()

    def verify_scrolling_feature(self):

        scroll_top_to_bottom = self.driver.execute_script("window.scrollBy(0,100000)")
        time.sleep(3)
        scroll_bottom_to_top = self.driver.execute_script("window.scrollBy(100000,0)")

    def scroll_the_page_till_element_found(self,By_locater):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By_locater))
        action = ActionChains(self.driver)
        action.move_to_element(bottom_element).perform()






