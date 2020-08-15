from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
options = Options()
options.add_argument("headless")
chrome_path = r"/Users/pranatikuppa/Desktop/random_words/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_path, options=options)
driver.get("https://reddit.com")


driver.quit()