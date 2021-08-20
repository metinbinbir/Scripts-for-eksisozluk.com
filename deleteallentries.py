import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


chrome= webdriver.Chrome()

chrome.get("https://eksisozluk.com/giris")
time.sleep(30)
profileButtonXPATH='//*[@id="top-navigation"]/ul/li[6]/a'
element=chrome.find_element_by_xpath(profileButtonXPATH)
element.click()
numberofEntries='//*[@id="profile-stats-section-content"]/h1/small'
element=chrome.find_element_by_xpath(numberofEntries).text
element=element.replace('(','').replace(')','')

for i in range(int(element)):
    toggleXPATH='//*[@id="entry-item-list"]/li/footer/div[2]/div'
    silButtonXPATH='//*[@id="entry-item-list"]/li/footer/div[2]/div/ul/li[3]'
    onayButtonXPATH='//*[@id="delete-self-form"]/fieldset/div[2]/button[1]'
    element=chrome.find_element_by_xpath(toggleXPATH)
    element.click()
    time.sleep(2)
    element=chrome.find_element_by_xpath(silButtonXPATH)
    element.click()
    time.sleep(2)
    element=chrome.find_element_by_xpath(onayButtonXPATH)
    element.click()
    time.sleep(36)
    profileButtonXPATH = '//*[@id="top-navigation"]/ul/li[6]/a'
    element = chrome.find_element_by_xpath(profileButtonXPATH)
    element.click()
