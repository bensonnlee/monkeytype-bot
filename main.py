from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def MonkeyType():
    url = "https://monkeytype.com/"
    driver.get(url)
    sleep(3)

    while True:
        try:
            active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")

            for char in active_word.text:
                ActionChains(driver).send_keys(char).perform()
            ActionChains(driver).send_keys(Keys.SPACE).perform()

        except Exception as e:
            print(e)
            break

if __name__ == '__main__':
    MonkeyType()

    input("Press any key to exit...")
    driver.quit()