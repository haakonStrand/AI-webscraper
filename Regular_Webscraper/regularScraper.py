#Python 3.11.2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests


class CurrentElectricityPriceTrondheim:
    '''
    A class used to contain information about electricity prices

    ...

    Attributes 
    -----------

    '''
    def __init__(self):
        '''
        Contstructor for the class, setting up the website url and parsing it
        
            Parameters:
                self : the object

        '''
        self.url = "https://www.hvakosterstrommen.no/i/trondheim"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, "html")
        self.info = ""
        self.priceNowTrondheim = 0
    
    def getPrice(self):
        '''
        Function finds the paragraph containing electricity price

            Parameters:
                self : the object

        '''
        self.info = self.soup.find("p", class_ = 'h1 mb-0').text.split()
        self.priceNowTrondheim = float(self.info[5].replace(",","."))
