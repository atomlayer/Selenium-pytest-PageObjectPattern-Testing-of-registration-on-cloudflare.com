# -*- coding: utf-8 -*-

from fixture.pages.page_base import PageBase
from fixture.pages.sign_up_page import SignUpPage
from selenium import webdriver

class HomePage(PageBase):


    signUpLink = '//ul[@class="top-nav__item-list top-nav__item-list--right"]//a[@data-tracking-label="signup"]'


    def open_home_page(self):
        self.browser.get("https://www.cloudflare.com/")
        return self

    def click_on_signUp_link(self):
        self.browser.find_element_by_xpath(self.signUpLink).click()
        return SignUpPage(self.browser)

