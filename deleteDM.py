from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def connect():
    browser = webdriver.Chrome()
    dmBoxURL = 'https://eksisozluk.com/mesaj'
    dmBoxXPATH = '//*[@id="top-navigation"]/ul/li[7]/a'
    browser.get(dmBoxURL)
    WebDriverWait(browser, 180).until(EC.visibility_of_element_located((By.XPATH, dmBoxXPATH)))
    deleteMessages(browser)
    browser.close()

def isMoreThan25DMs(xpath, browser):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def pageNumber(browser):
    messagePageXPATH = '//*[@id="message-thread-list-form"]/div[1]/a[1]'
    checkBoxXPATH = '//*[@id="threads"]/li[1]/article/input'
    if (isMoreThan25DMs(messagePageXPATH, browser)):
        messagePageCount = browser.find_element_by_xpath(messagePageXPATH).text
        messagePageCount.replace("(", "")
        messagePageCount.replace(")", "")
        return int(messagePageCount)
    else:
        if(isMoreThan25DMs(checkBoxXPATH,browser)==False):
            print("Your DM Box is already empty!")
            return 0
        return 1

def deleteMessages(browser):
    deleteButton = '//*[@id="message-thread-list-form"]/p[2]/button[1]'
    confirmationButton = '//*[@id="confirmyes"]'
    pageCount = pageNumber(browser)
    for i in range(pageCount):
        checkBoxes = browser.find_elements_by_name("threadId")
        for checkbox in checkBoxes:
            checkbox.click()
        browser.find_element_by_xpath(deleteButton).click()
        try:
            WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.XPATH,confirmationButton))).click()
        except (NoAlertPresentException, TimeoutException):
            pass



connect()