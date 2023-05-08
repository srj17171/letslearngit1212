from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    login_click_xpath = "//a[normalize-space()='Login']"
    email_textbox_xpath = "//input[@id='email']"
    password_textbox_xpath = "//input[@id='password']"
    login_btn_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.login_click_xpath).click()
        self.driver.find_element(By.XPATH,self.email_textbox_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_click_xpath).click()
