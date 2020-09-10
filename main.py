from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#/Users/tootles/Desktop/chromedriver
path = input("Chromedriver path: ")
PATH = path
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(1)

cookie = driver.find_element_by_id("bigCookie")
numCookies = driver.find_element_by_id("cookies")

actions = ActionChains(driver)
actions.click(cookie)

for i in range(20):
    actions.perform()

upgrades = [driver.find_element_by_id("productPrice"+ str(i)) for i in range (1, -1, -1)]

for i in range(5000):
    actions.perform()
    count = int(numCookies.text.split(" ")[0])
    print(count)
    for upgrade in upgrades:
        value = int(upgrade.text)
        if value <= count:
            upgradeAction = ActionChains(driver)
            upgradeAction.move_to_element(upgrade)
            upgradeAction.click()
            upgradeAction.perform()

driver.quit()