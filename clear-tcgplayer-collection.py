from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = "{path}\chromedriver.exe"
TCGPLAYER_EMAIL = "email@email.com"
TCGPLAYER_PASSWORD = "password"
MAX_CLICK = 50 #Largest number in your collection
SLEEP_TIME = 5 #Varies with internet speed. 5 is default

class TcgplayerCollectionClearer:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.tcgplayer.com/login?returnUrl=store.tcgplayer.com%2Fcollection")

        sleep(SLEEP_TIME)
        email = self.driver.find_element_by_name("Email")
        email.send_keys(TCGPLAYER_EMAIL)

        password = self.driver.find_element_by_name("Password")
        password.send_keys(TCGPLAYER_PASSWORD)

        sleep(SLEEP_TIME)
        password.send_keys(Keys.RETURN)

        sleep(SLEEP_TIME)
    
    def clear_collection(self):
        down_arrows = self.driver.find_elements_by_class_name("CollectionDownArrow")

        for arrow in down_arrows:
            for i in range(MAX_CLICK):
                try:
                    arrow.click()
                except:
                    pass

collection_clearer = TcgplayerCollectionClearer()
collection_clearer.login()
collection_clearer.clear_collection()
