from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule
import datetime

options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# set webdriver path here it may vary
# browser = webdriver.Chrome("F:/C Programming/Python/chromedriver.exe")

website_URL = "https://web.whatsapp.com/"
driver.get(website_URL)

driver.maximize_window()
time.sleep(10)

# l = driver.get("https://web.whatsapp.com/send?phone=8511830100&text=Hii")
search = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]/div/div[1]/p")))
# search.click()
# driver.refresh()
search.send_keys("Mayank Bhai ")
search.send_keys(Keys.RETURN)
time.sleep(2)

# tick = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]")))
# tick.click()
# time.sleep(2)

def hello():
    msg = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    msg.send_keys("Hii")
    msg.send_keys(" Hello Brother! Happy Labh Pancham!")
    msg.send_keys(Keys.RETURN)


# schedule.every().day.at("11:41").do(hello)

# Schedule the job to run every 2 seconds
# schedule.every(5).seconds.do(hello)

# scheduling the hello to run every 5 seconds for 3 times
i = 0
while(i<3):
        schedule.every(5).seconds.do(hello)
        i += 1
        
while True:
    schedule.run_pending()
    time.sleep(1)