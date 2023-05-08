from Pageobject.Loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Test_001:
    nurl = "https://automation.credence.in/"
    email = "test@credence.in"
    password = "test@123"

    def test_login(self):
        webdriver_service = Service(executable_path="testcases/chromedriver.exe")
        driver = webdriver.Chrome(service=webdriver_service)
        driver = webdriver.Chrome()
        lp = LoginPage(driver)
        driver.get(self.nurl)
        lp.set_username(self.email)
        lp.set_password(self.password)
        lp.click_login()
        title = driver.title
        if title == "CredKart":
            assert True
        else:
            assert False
