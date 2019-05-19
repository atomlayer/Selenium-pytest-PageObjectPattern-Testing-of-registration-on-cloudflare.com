# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.pages.page_base import PageBase

class SignUpPage(PageBase):


    get_started_with_cloudflare_label = "//h1[@class='c_ed c_at c_ee c_ef c_eg c_eh']/span"

    email_input="//input[@name='email']"

    password_input = "//input[@name='password']"

    create_account_button = "//button[@data-testid='signup-button']"

    error_alert = '//span[@class="c_bm c_is c_ah c_c c_q"]'

    def open_sign_up_page(self):
        self.browser.get("https://dash.cloudflare.com/sign-up")
        return self

    def get_value_of_started_with_cloudflare_label(self):
        return self.browser.find_element_by_xpath(self.get_started_with_cloudflare_label).text

    def pass_email(self, email):
        self.browser.find_element_by_xpath(self.email_input).send_keys(email)
        return self

    def pass_passord(self, passord):
        self.browser.find_element_by_xpath(self.password_input).send_keys(passord)
        return self

    def create_account(self):
        self.browser.find_element_by_xpath(self.create_account_button).click()
        return self

    def get_error_alert(self):
        return self.browser.find_element_by_xpath(self.error_alert).text

