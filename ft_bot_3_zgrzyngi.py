from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://footballteam.pl')

browser.find_element_by_xpath('//*[@id="buttons"]/div/button[1]').click()
browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[1]/div[1]').click()
username = browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[2]/div/form/div[1]/input')
password = browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[2]/div/form/div[2]/input')
username.send_keys('granat29@vp.pl')
password.send_keys('qwerty123')
browser.find_element_by_xpath('//*[@id="btn-login"]').click()

browser.maximize_window()
browser.implicitly_wait(5)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/aside/ul/li[2]/a').click()
browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/ul/li[5]/a').click()

try:
    free_keys = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(2) > div.overflow-hidden > main > div > div > div > div > div:nth-child(2) > div.tb-body.overlay > div.w-full.h-full.overflow-x-hidden > div > div.mb-4.pack.shop-item--item.shop-item--item-free > div > div')))
    free_keys = int(free_keys.get_attribute('textContent'))
except:
    print("dupa")

bronze = int(browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/div/div[4]/div[1]/div[2]/div[1]/div/div/div/div').get_attribute("textContent"))
silver = int(browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/div/div[5]/div[1]/div[2]/div[1]/div/div/div/div').get_attribute("textContent"))

while silver > 0 and free_keys > 0:
        try:
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div/div[5]/div[1]/div[2]/div[1]/div/button[1]'))).click()
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div/div[5]/div[2]/div/div/div[2]/div[1]/div[2]/div/button'))).click()
            silver -= 1
            free_keys -= 1
            browser.refresh()
            browser.implicitly_wait(1)
        except:
            pass

while bronze > 0 and free_keys > 0:
        try:
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div/div[4]/div[1]/div[2]/div[1]/div/button[1]'))).click()
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/div/div/div[4]/div[2]/div/div/div[2]/div[1]/div[2]/div/button'))).click()
            bronze -= 1
            free_keys -= 1
            browser.refresh()
            browser.implicitly_wait(1)
        except:
            pass

#if __name__ == '__main__':