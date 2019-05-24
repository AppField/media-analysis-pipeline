#Originalcode: https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

#Hier aufpassen! Das ist mein Pfad zum chromedriver.exe! Wird bei euch nicht funktionieren. Anpassen falls notwendig.
browser = webdriver.Chrome(executable_path=r"C:\Users\Filip\Desktop\chromedriver.exe", chrome_options=option)  
browser.get(r"https://github.com/TheDancerCodes")

# Wait 5 seconds for page to load
timeout = 5

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full height-full rounded-2']")))
    

except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# find_elements_by_xpath returns an array of selenium objects.

titles_element = browser.find_elements_by_xpath("//a[@class='text-bold flex-auto ']")

# use list comprehension to get the actual repo titles and not the selenium objects.

titles = [x.text for x in titles_element]

# print out all the titles.

print('titles:')
print(titles, '\n')

    
language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")

# same concept as for list-comprehension above.
languages = [x.text for x in language_element]

print("languages:")
print(languages, '\n')

for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')