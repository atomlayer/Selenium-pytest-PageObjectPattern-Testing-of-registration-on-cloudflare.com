# -*- coding: utf-8 -*-

from selenium import webdriver



class App:
    def __init__(self):
        geckodriver = 'C:\selenium\\geckodriver.exe'
        options = webdriver.FirefoxOptions()
        self.browser = webdriver.Firefox(executable_path=geckodriver, options=options)
        self.browser.implicitly_wait(30)


    def tearDown(self):
        self.browser.quit()

