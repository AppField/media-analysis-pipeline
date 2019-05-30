from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys

option = webdriver.FirefoxOptions()
#option.add_argument("-private")

url = sys.stdin.readline()                

#url zum testen:
#url = "https://derstandard.at/2000103980412/Salvinis-Triumph-hinterlaesst-in-Italien-Freund-und-Feind-ratlos"        

#path für ubuntu:
#browser = webdriver.Firefox(executable_path=r"Geckodriver", firefox_options=option)  
browser = webdriver.Firefox(executable_path=r"C:\Windows\System32\WebDriver\geckodriver.exe", firefox_options=option)  
browser.get(url)

# Wait 5 seconds for page to load
timeout = 5

browser.find_element_by_xpath("/html/body/main/section/div/div[1]/button").click()

try:
     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.ID, "navLine1")))
    

except TimeoutException:
     print("Timed out waiting for page to load")
     browser.quit()

# find_elements_by_xpath returns an array of selenium objects.

# titles_element = browser.find_elements_by_css_selector("li[id^='nav']")

# # use list comprehension to get the actual repo titles and not the selenium objects.

# titles = [x.text for x in titles_element]

# print out all the titles.

# print('titles:')
# print(titles, '\n')

# browser.find_element_by_xpath("//a[@href='/Wissenschaft?ref=nav_haupt']").click()

# articlelist = browser.find_elements_by_xpath("//li[@class='big img']")
# articlelist += browser.find_elements_by_xpath("//li[@class='normal img']") #nicht vollständige aufzählung

# articles = [x.text for x in articlelist]

# print out all the articles. 

# print('list of articles:')
# print(articles, '\n')

# browser.find_element_by_xpath("//li[@class='big img']").click()

# article_text = browser.find_elements_by_xpath("//div[@class='copytext']//p")

# text = [x.text for x in article_text]

# # print out all the titles.

# print('article text:')
# print(text, '\n')

# browser.back()
# browser.implicitly_wait(4)

# browser.find_element_by_xpath("//ul[@class='stories col-A']/li[3]/div[2]/h3/a").click()

article_text = browser.find_elements_by_xpath("//div[@class='copytext']//p")

text = [x.text for x in article_text]

# print out all the titles.

print('article text: \n')
print(text, '\n')

# browser.back()
# #browser.implicitly_wait(4)

# browser.find_element_by_xpath("//ul[@class='stories col-A']/li[4]/div[2]/h3/a").click()

# article_text = browser.find_elements_by_xpath("//div[@class='copytext']//p")

# text = [x.text for x in article_text]

# # print out all the titles.

# print('\n\n\narticle text:')
# print(text, '\n')
