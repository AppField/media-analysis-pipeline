from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.FirefoxOptions()
option.add_argument("-private")

#Hier aufpassen! Das ist mein Pfad zum chromedriver.exe! Wird bei euch nicht funktionieren. Anpassen falls notwendig.
browser = webdriver.Firefox(executable_path=r"C:\Windows\System32\WebDriver\geckodriver.exe", firefox_options=option)  
browser.get(r"https://diepresse.com/")

# Wait 5 seconds for page to load
timeout = 5

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//nav[@class='primary-nav priority-nav priority-nav-has-dropdown']")))
    

except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# find_elements_by_xpath returns an array of selenium objects.

titles_element = browser.find_elements_by_xpath("//ul[@class='primary-nav__menu js-dropdown']")

# use list comprehension to get the actual repo titles and not the selenium objects.

titles = [x.text for x in titles_element]

# print out all the titles.

print('titles:')
print(titles, '\n')

browser.find_element_by_xpath("//a[@href='/home/techscience']").click()

articlelist = browser.find_elements_by_xpath("//a[@class='b__link--full']")

articles = [x.text for x in articlelist]

# print out all the titles. funktioniert noch nicht so wie es sollte

print('list of articles:')
print(articles, '\n')

browser.find_element_by_xpath("//a[@class='b__link--full']").click()

article_text = browser.find_elements_by_tag_name('p')

text = [x.text for x in article_text]

# print out all the titles.

print('article text:')
print(text, '\n')
