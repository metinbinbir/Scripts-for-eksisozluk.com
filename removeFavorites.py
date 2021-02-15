import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def RemoveSmallerThan10(favcount,unfavButtonXPATH,browser):
        links=browser.find_elements_by_xpath(unfavButtonXPATH)
        for link in links:
            link.click()
            time.sleep(4)


def RemoveBiggerThan10(favcount,unfavButtonXPATH,browser):
    favUntilXPATH='//*[@id="user-profile-stat-caption"]'
    loop=int(favcount/10)
    for i in range(loop):
        links=browser.find_elements_by_xpath(unfavButtonXPATH)
        for link in links:
            link.click()
            time.sleep(4)
        links.clear()
        WebDriverWait(browser,180).until(EC.element_to_be_clickable((By.XPATH,favUntilXPATH))).click()

browser= webdriver.Chrome()
browser.get("https://eksisozluk.com/mesaj")
profileButtonXPATH='//*[@id="top-navigation"]/ul/li[6]/a'
favsButtonXPATH='//*[@id="profile-stats-section-nav"]/li[2]/a'
favsCountXPATH='//*[@id="profile-stats-section-content"]/h1/small'
favUntilXPATH='//*[@id="user-profile-stat-caption"]'
unfavButtonXPATH='//*[@id="entry-item-list"]/li/footer/div[1]/span[3]/a[1]'

element = WebDriverWait(browser, 180).until(EC.visibility_of_element_located((By.XPATH,profileButtonXPATH)))
browser.find_element_by_xpath(profileButtonXPATH).click()

element=WebDriverWait(browser,180).until(EC.visibility_of_element_located((By.XPATH,favsButtonXPATH)))
browser.find_element_by_xpath(favsButtonXPATH).click()

element=WebDriverWait(browser,180).until(EC.text_to_be_present_in_element((By.XPATH,favUntilXPATH),"favori entry'leri"))
favsCount=browser.find_element_by_xpath(favsCountXPATH).text
favsCount=favsCount.replace("(","")
favsCount=favsCount.replace(")","")
favsCount=int(favsCount)
favsCountMOD10=favsCount%10


while(1):
    if(favsCount>=10):
        RemoveBiggerThan10(favsCount,unfavButtonXPATH,browser)
        RemoveSmallerThan10(favsCount,unfavButtonXPATH,browser)

    else:
        RemoveSmallerThan10(favsCount,unfavButtonXPATH,browser)






