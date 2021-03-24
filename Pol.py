import os
import discord
from dotenv import load_dotenv
import requests
from requests import Session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import date
import schedule
from discord import Webhook, RequestsWebhookAdapter
import re

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver' 
GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

webhook = Webhook.partial(823976320031129652, '0lm7Cvs-AebhinVqtzJTJtlEEKhC19LKSp8nug3LZqEOMKYG-A7e_mXjnntSbUkifQkG', adapter=RequestsWebhookAdapter())

def login():
    browser.get('https://footballteam.pl')
    browser.find_element_by_xpath('//*[@id="buttons"]/div/button[1]').click()
    browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[1]/div[1]').click()
    username = browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[2]/div/form/div[1]/input')
    password = browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[2]/div/form/div[2]/input')
    username.send_keys('granat29@vp.pl')
    password.send_keys('qwerty123')
    browser.find_element_by_xpath('//*[@id="btn-login"]').click()

def logout():
    profile = browser.find_element_by_xpath('/html/body/div[1]/div[1]/header/div[1]/div[2]')
    ActionChains(browser).move_to_element(profile).perform()
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/header/div[1]/div[2]/div[1]/ul/li[5]/a').click()
    
def getTask():
    browser.get('https://pl.footballteamgame.com/dashboard')
    browser.refresh()
    task = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[3]/div[2]/div[1]/div/div[2]/p")))
    task_formated = task.get_attribute("textContent")
    webhook.send("@Mesie Muszi Zadanie na " + date.today().strftime("%d/%m/%Y") + " : " + task_formated.strip())

def clubTraining():
    webhook.send("@everyone Trening klubowy! (☞ﾟヮﾟ)☞")
    
def getMatch():
    browser.get('https://pl.footballteamgame.com/dashboard')
    browser.implicitly_wait(5)
    match = browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/div[5]/div[2]/div[1]/div/div[1]/div/div[2]').get_attribute("textContent")
    match = match.strip()
    match = match[12:]
    #match = f'"{match}"' 
    schedule.every().day.at(match).do(matchNotification)

def matchNotification():
    webhook.send("TeXDsty na prodXDukcji Mecz sparingowy! XD")

schedule.every().day.at("19:00").do(login)
schedule.every().day.at("09:30").do(getTask)
schedule.every().day.at("19:10").do(getMatch)
schedule.every().day.at("20:00").do(clubTraining)
schedule.every().day.at("22:00").do(logout)

@client.event
async def on_ready():
    while True:
        schedule.run_pending()
        time.sleep(1)

client.run(TOKEN)


