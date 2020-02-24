'''
Created on 16 feb. 2020

@author: Miguel
'''

import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep, time
import string
from random import randint

USER_DATA_DIR = "C:\\Users\\Miguel\\AppData\\Local\\Google\\Chrome\\"

def generateKey():
    _ms = int(1000* round(time()))
    _ms = randint(0,100) * _ms + randint(0,1000)
    
    key = str(_ms) 
    for _ in range(5):
        key = list(key)
        key[randint(0, len(key)- 1)] = string.ascii_letters[randint(0, 51)] 
        key = "".join(key)
    return key

class BookingBot(object):
    '''
    classdocs
    Abstract class to declare basic actions on web
    '''
    GOOGLE_URL    = "https://google.com"
    MAIN_PAGE_URL = "https://google.com"
    SAVING_FOLDER = "results/"
    RESULTS_FILE  = ""
    
    class StatusEnum:
        UNSTARTED = "unstarted"
        FAILED    = "failed"
        SUCCEDED  = "succeded"
        SKIPPED   = "skipped"
        
    
    @classmethod
    def __new__(cls, *args):
        cls.__driverOptions = webdriver.ChromeOptions()
        cls.__driverOptions.add_argument(USER_DATA_DIR)
        return super(BookingBot, cls).__new__(cls)
    
    def __init__(self, *args):
        # init driver
        self.status = self.StatusEnum.UNSTARTED
        self.driver = webdriver.Chrome(os.environ['CHROMEDRIVER_PATH'], 
                                       chrome_options=self.__driverOptions)
        self._fuckReCaptcha()
        self.driver.get(self.GOOGLE_URL)
        sleep(2)
        try:
            self.driver.get(self.MAIN_PAGE_URL)
            sleep(2)
            self._automatedActionsOnPage()
        except Exception as err:
            self.status = self.StatusEnum.FAILED
            print(err.message())
        finally:
            self._saveValues()
        
    
    def _fuckReCaptcha(self):
        """ Generate random browswerClient"""
        
        session = requests.Session()
        headers =  {"User-Agent":  'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
                                   'AppleWebKit/537.36 (KHTML, like Gecko)'
                                   'Chrome/80.0.3987.116 Safari/537.36',
                    "Accept": 'text/html,application/xhtml+xml,application/xml;'
                                'q=0.9,image/webp,image/apng,*/*;q=0.8'}
        url = 'https://www.whatismybrowser.com/developers/'\
                'what-http-headers-is-my-browser-sending'
        req = session.get(url, headers=headers)
        bs  = BeautifulSoup(req.text, 'html.parser')
        print(bs.find('table', {'class': 'table-striped'}).get_text)
        
#         key = generateKey()
#         self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", 
#                                     {"headers":{"User-Agent": f"{key}"}})
    
    def _automatedActionsOnPage(self):
        raise Exception("abstract method, please fill me.")
    
    def _defineVariables(self):
        pass
    def _saveValues(self):
        if self.status == self.StatusEnum.SUCCEDED:
            if not os.path.isdir(self.SAVING_FOLDER):
                os.makedirs(self.SAVING_FOLDER)
            if 
            
        
#     @abstractmethod
#     def login(self):
#         pass
#     @abstractmethod
#     def log_out(self):
#         pass
#     
#     @abstractmethod
#     def pressButton(self):
#         pass
#     
#     @abstractmethod
#     def fillEntrance(self):
#         pass
#     
#     @abstractmethod
#     def getField(self):
#         pass
    

        