import requests
import schedule
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from requests.exceptions import RequestException


#Exception Errors Classifications

class WebPageOpenError(Exception):
    def __init__(self, message="Web page could not open."):
        self.message = message
        super().__init__(self.message)
        
class SearchError(Exception):
    def __init__(self, message="Video could not be found."):
        self.message = message
        super().__init__(self.message)
        
class MoreInfoError(Exception):
    def __init__(self, message="Hyperlink could not be found in 'More Info' section."):
        self.message = message
        super().__init__(self.message)
        

class CloseExcessWindowsError(Exception):
    def __init__(self, message="Excess windows could not be closed."):
        self.message = message
        super().__init__(self.message)
        
class ExcelFileDownloadError(Exception):
    def __init__(self, message="Excel file could not be downloaded."):
        self.message = message
        super().__init__(self.message)


# Webdriver automation


class download_data:

    
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox") # Required to use selenium with Docker
        options.add_argument("--disable-dev-shm-usage") # Prevent resource issues
        options.add_argument("--disable-gpu")
        options.add_argument("--disable extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start--maximized")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(8)
        
    
    def open_browser(self):
        try:
            self.driver.get('https://www.youtube.com/')

        except Exception as e:
            raise WebPageOpenError(f'Error!: {e}') 
            
        else:
            print("Browser successfully opened.")
            
            
    def search_and_open_video_page(self):
        try:
            search = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.NAME,"search_query"))
            )
            search.send_keys("the only excel portfolio project you need mo chen",Keys.RETURN)
            video = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT,"The ONLY EXCEL PORTFOLIO PROJECT YOU NEED")
            ))
            video.click()  

        except Exception as e:
            raise SearchError(e)
            
        else:
            print('Video page successfully opened.')

    def more_info_hyperlink(self):
        try:
            more_info = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID,"snippet")
                ))
            more_info.click()
            github_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"//github.com/mochen862/"))
            )
            github_link.click()

        except Exception as e:
            raise MoreInfoError(f'Error!: {e}')
            
        else:
            print('More info hyperlink successfully opened.')

    def close_excess_windows(self):

        try:
            # Find the name of and switches to the second window, Github repository
            windows = self.driver.window_handles
            for window in windows:
                self.driver.switch_to.window(window)

            self.driver.switch_to.window(windows[0])  # Switch back to YouTube window
            self.driver.close() #closes YouTube window
            self.driver.switch_to.window(window)  # Switch back to Github window

        except Exception as e:
            raise CloseExcessWindowsError(f'Error! {e}')
            
        else:
            print('Excess windows successfully closed.')

    def download_file(self):
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT,"coffeeOrdersData").click()
            self.driver.find_element(By.LINK_TEXT,"View raw").click()

        except Exception as e:
            raise ExcelFileDownloadError(f'Error!: {e}')
            
        else:
            print('Excel file successfully downloaded.')

    def execute(self):
        try:
            self.open_browser()
            sleep(3)
            self.search_and_open_video_page()
            sleep(5)
            self.more_info_hyperlink()
            sleep(3)
            self.close_excess_windows()
            sleep(3)
            self.download_file()
            sleep(3)
            self.driver.quit()
        
        except (WebPageOpenError, SearchError, MoreInfoError, CloseExcessWindowsError, ExcelFileDownloadError) as e:
            print(f'Stopped due to error: {e}')


if __name__ == "__main__":
    browser_bot = download_data()  # Instantiate the bot
    browser_bot.execute()         # Start the bot execution

