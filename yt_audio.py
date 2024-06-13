from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Music:
    def __init__(self):
        self.query = None
        service = Service(
            'C:/Users/Rutuja Gurav/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)

        # Wait for user input to keep the browser open

        # Find the search input element and perform the search
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        # search.click()
        # search.send_keys(query)
        #
        # # Find the search button and click it
        # enter = self.driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
        video.click()
        input("Press Enter to continue with the search...")


# Example usage:
# assist = Music()
# assist.play('dynamite')




