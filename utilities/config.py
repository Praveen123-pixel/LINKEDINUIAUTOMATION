from utilities.Generic import Test_generic


class Test_Config(Test_generic):
    def __int__(self):
       pass
    def Launch_the_Application(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    def close_the_application(self):
        self.driver.close()