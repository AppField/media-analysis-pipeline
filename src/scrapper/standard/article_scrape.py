from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys

option = webdriver.FirefoxOptions()
#option.add_argument("-private")
option.headless = True

#url = sys.stdin.readline()                

#url zum testen:
url = "https://derstandard.at/2000103980412/Salvinis-Triumph-hinterlaesst-in-Italien-Freund-und-Feind-ratlos"        

#path für ubuntu:
browser = webdriver.Firefox(executable_path="./geckodriver", firefox_options=option)  
#browser = webdriver.Firefox(executable_path=r"C:\Windows\System32\WebDriver\geckodriver.exe", firefox_options=option)  
browser.get(url)

# Wait 10 seconds for page to load
timeout = 10

browser.find_element_by_xpath("/html/body/main/section/div/div[1]/button").click()

try:
     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.ID, "navLine1")))
    

except TimeoutException:
     print("Timed out waiting for page to load")
     browser.quit()

# find text from article

article_text = browser.find_elements_by_xpath("//div[@class='copytext']//p")

text = [x.text for x in article_text]

# print out all the titles.

print('article text: \n')
print(text, '\n')

browser.quit()
