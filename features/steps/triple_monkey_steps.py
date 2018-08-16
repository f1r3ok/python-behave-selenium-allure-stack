# Step deifinition file
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from allure_commons.types import AttachmentType
import time, allure

@given(u'the user opens Triple Monkey')
def step_impl(context):
    # Open game url
    context.webdriver.get(context.test_data['base_url'])

@when(u'user press Play button')
def step_impl(context):
    # Wait for Play button
    for i in range(40):
        time.sleep(1)
        try:
            if True == context.webdriver.execute_script('return c_button && c_button.worldVisible && c_button.emit("click")'):
                print('\nTried for ' + str(i) + ' seconds.' + '\n')
                break
                return
        except WebDriverException:
            continue

@then(u'user get start balance')
def step_impl(context):
    context.start_balance = context.webdriver.find_element_by_xpath("//div[@class='footer-balance-value']").text[1:]

@then(u'user send cheat')
def step_impl(context):
    context.webdriver.execute_script("document.getElementsByClassName('combinations-toggle')[0].click();")
    context.webdriver.execute_script("document.getElementsByClassName('combinations-input-field')[0].value='1,3,7';")
    context.webdriver.execute_script("document.getElementsByClassName('combinations-input-ok')[0].click();")
    context.webdriver.execute_script("document.getElementsByClassName('combinations-toggle')[0].click();")

@then(u'user get total bet')
def step_impl(context):
    context.total_bet = context.webdriver.execute_script("return c_totalbetLabel.text")[1:]

@then(u'user press Spin button')
def step_impl(context):
    context.webdriver.execute_script("c_spinButton.emit('click')")
    time.sleep(3)

@then(u'user get end balance')
def step_impl(context):
    context.end_balance = context.webdriver.find_element_by_xpath('//div[@class="footer-balance-value"]').text[1:]

@then(u'user compares start and end balance')
def step_impl(context):
    print('context.start_balance: ' + context.start_balance + '\n')
    print('context.end_balance: ' + context.end_balance + '\n')
    print('context.total_bet: ' + context.total_bet + '\n')
    assert float(context.end_balance) == (float(context.start_balance) - 2 * float(context.total_bet))
    allure.attach(context.webdriver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
