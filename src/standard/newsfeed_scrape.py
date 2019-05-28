from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.FirefoxOptions()
#option.add_argument("-private")

#Hier aufpassen! Das ist mein Pfad zum geckodriver.exe! Wird bei euch nicht funktionieren. Anpassen falls notwendig.
browser = webdriver.Firefox(executable_path=r"C:\Windows\System32\WebDriver\geckodriver.exe", firefox_options=option)  
browser.get(r"https://derstandard.at/?_chron=t")

# Wait 5 seconds for page to load
timeout = 5

browser.find_element_by_xpath("/html/body/main/section/div/div[1]/button").click()

try:
     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.ID, "navLine1")))
    

except TimeoutException:
     print("Timed out waiting for page to load")
     browser.quit()

urlsh3 = browser.find_elements_by_xpath("//div[@id='mainContent']//li[contains(@data-id, '200')]//h3/a")
urlsh4 = browser.find_elements_by_xpath("//div[@id='mainContent']//li[contains(@data-id, '200')]//h4/a")

text = [x.get_attribute("href") for x in urlsh3]
text += [x.get_attribute("href") for x in urlsh4]

# print out all the urls.

for x in text:
     print(x)
     