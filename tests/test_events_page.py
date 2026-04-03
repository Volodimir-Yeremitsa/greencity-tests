from concurrent.futures import wait
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys





class TestGreenCity(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):    # виконується перед кожним тестом

        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)      # глобальне налаштування очікування елементів.
                                            # Після цього всі find_element будуть чекати до 3 секунд
                                            # 0 не використовувати взагалі
        self.wait = WebDriverWait(self.driver, 10)  # явне очікування, яке можна використовувати для конкретних елементів                                        
                                                     # self.wait.until(...)   
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_Events_Page_Display(self):

        card_xpath = "//*[contains(@class,'card-wrapper') ]"
        card = self.driver.find_element(By.XPATH, card_xpath)
        self.assertTrue(card.is_displayed(), "Список івентів не відображається")


    def test_Navigation_to_Event_Details(self):
        
        # Step 1: Open Events page  = test_events_page
        card_xpath = "//*[contains(@class,'card-wrapper')]"
        cards = self.driver.find_elements(By.XPATH, card_xpath)
        self.assertTrue(len(cards) > 0, "Список івентів не відображається")

        # Step 2: Click "More" on first event
        more_button_xpath = "(//button[contains(normalize-space(), 'Більше') or contains(normalize-space(), 'More')])[1]"
        more_button = self.driver.find_element(By.XPATH, more_button_xpath)
        more_button.click()

        # Step 3: Check event details page
        # details_xpath = "//*[contains(@class,'event-info-block')]"
        details_selector = ".event-info-block"
        details = self.driver.find_element(By.CSS_SELECTOR, details_selector)
        self.assertTrue(details.is_displayed(), "Деталі івенту не відображаються")

    def test_Event_Search_Functionality(self):
        
        # Step 1:  Open the Events page 
        card_xpath = "//*[contains(@class,'card-wrapper')]"
        # cards = self.driver.find_elements(By.XPATH, card_xpath)
        cards = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, card_xpath))
        )        
        self.assertTrue(len(cards) > 0, "Список івентів не відображається")

        # Step 2:  
        # Клік по іконці пошуку
        search_img_xpath = "//span[@class='search-img']"
        search_img = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, search_img_xpath))
        )        
        search_img.click()

        # чекати input  
        # CSS_SELECTOR, "input.place-input"
        search_input_xpath = "//input[contains(@class,'place-input')]"
        search_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, search_input_xpath))
        )
        search_input.send_keys("s")

        # Щось знайшли?
        card_xpath = "//*[contains(@class,'card-wrapper')]"
        # cards = self.driver.find_elements(By.XPATH, card_xpath)
        cards = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, card_xpath))
        )
        self.assertTrue(len(cards) > 0, "Список івентів порожній після пошуку")

        # Step 3: 
        # Очистка Clear the search field
        search_input.clear()
        search_input.send_keys(" ")
        search_input.clear()        
        
        # sleep(5)  
        

if __name__ == "__main__":
    unittest.main()
    