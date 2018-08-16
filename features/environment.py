from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def before_all(context):
    context.test_data = json.load(open('features/test_data.json'))
    
    chrome_options = Options()
#    chrome_options.add_argument('disk-cache-dir=/home/f1r3ok/.cache/google-chrome/Default/Cache/')
#    chrome_options.add_experimental_option( "prefs", {'profile.default_content_setting_values.notifications': 2})
    # chrome_options.add_experimental_option( "prefs", {'profile.managed_default_content_settings.images': 2})
    
    context.webdriver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    context.webdriver.implicitly_wait(30)
    context.webdriver.set_page_load_timeout(30)
    
def after_all(context):
    context.webdriver.title
    #context.webdriver.quit()
