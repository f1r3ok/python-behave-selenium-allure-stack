from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def before_all(context):
    context.test_data = json.load(open('features/test_data.json'))   
    chrome_options = Options()    
    context.webdriver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    context.webdriver.implicitly_wait(30)
    context.webdriver.set_page_load_timeout(30)
    
def after_all(context):
    context.webdriver.title
