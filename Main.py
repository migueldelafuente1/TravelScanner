'''
Created on 16 feb. 2020

@author: Miguel
'''

from bookingBots.WebDriver import SkyScannerBookingBot

class Main(object):
    
    def __init__(self):
        ## load specification payloads for tracking
        
        ## initialize bots
        
        ## start tracking process
        ##    > enter in the webs, set specifications
        ##    > do actions to search the flight
        ##    > get the price and append it to a csv file
        ##    > repeat after certain time
        sksc = SkyScannerBookingBot()
        
        """ TODO: use context manager for the drivers
        with SkyScannerBookingBot() as sksc:
            sksc ...
        """
    
        sksc.close()
    
if __name__ == '__main__':
    Main()
    