'''
Created on 24 feb. 2020

@author: Miguel
'''
from bookingBots.WebDriver import BookingBot

class KayakBookingBot(BookingBot):
    
    MAIN_PAGE_URL = "https://www.skyscanner.es/"#"https://www.uam.es"#
    
    def _automatedActionsOnPage(self):
        self.__manageCookiesScreen()
        sleep(300)
    
    def __manageCookiesScreen(self):
        
        self.driver.get_cookies()
        print(self.driver.window_handles)    

  