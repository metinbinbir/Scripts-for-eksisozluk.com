from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

def howManyBlocked(xpathLink,browser):
    string = browser.find_element_by_xpath(xpathLink).text
    stringToList = []
    i = 0
    while (string[i] != " "):
        stringToList.append(str(string[i]))
        i += 1
    emptyString = ""
    number = emptyString.join(stringToList)
    return number

def unblockUser(xpathLinkOfSilButton,browser,url):
    browser.find_element_by_xpath(xpathLinkOfSilButton).click()
    try:
        WebDriverWait(browser, 5).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        browser.implicitly_wait(1.75)
        alert.accept()
    except (NoAlertPresentException, TimeoutException):
        pass
    browser.get(url)

url="https://eksisozluk.com/takip-engellenmis"
xpathLinkOfNumber='//*[@id="content-body"]/div[2]/p'
xpathOfSilButton="//*[@id='content-body']/div[2]/ul/li[1]/span/a[2]"
browser=webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(120)
numberOfBlockedPerson=howManyBlocked(xpathLinkOfNumber,browser)

if(numberOfBlockedPerson!="yok"):
    while int(numberOfBlockedPerson)!=1:
        unblockUser(xpathOfSilButton,browser,url)
        browser.implicitly_wait(1.5)
        numberOfBlockedPerson=howManyBlocked(xpathLinkOfNumber,browser)

    unblockUser(xpathOfSilButton,browser,url)
    browser.close()
    print("Engel listeniz artık boş. / Your block list is empty now.")

else:
    print("Engel listeniz zaten boş. / Your block list is already empty.")
    browser.close()


