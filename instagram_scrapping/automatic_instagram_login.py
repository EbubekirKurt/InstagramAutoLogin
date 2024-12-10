from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')


class InstagramLogin():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        emailInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(5)

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button/div/div")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin.")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,'//button[text()="Unfollow"]').click()
        else:
            print("Zaten takip etmiyorsunuz.")


instagram = InstagramLogin()
instagram.login()

instagram.followUser("kod_evreni")
time.sleep(5)
instagram.unFollowUser("kod_evreni")
