#Python 3.11.2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests
import matplotlib as mpl
import math
from PIL import Image


class CurrentElectricityPriceTrondheim:
    '''
        A class used to contain information about electricity price
    '''
    def __init__(self):
        '''
        Contstructor for the class, setting up the website url and parsing it
        
            Parameters:
                self : the object

        '''
        self.url = "https://www.hvakosterstrommen.no/i/trondheim"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text,features="lxml")
        self.info = ""
        self.priceNowTrondheim = 0
        # A map of rgb points in your distribution
        # [distance, (r, g, b)]
        # distance is percentage from left edge
        self.heatmap = [
            [0.0, (0, 1, 0)],
            [0.20, (0, 0.5, .25)],
            [0.40, (0, 0.25, 0.5)],
            [0.60, (0.25, 0, 0.25)],
            [0.80, (0.5, 0, 0)],
            [0.90, (0.75, 0, 0)],
            [1.00, (1, 0, 0)],
        ]
        self.width, self.height = 1000, 200
        self.im = Image.new('RGB', (self.width, self.height))
        self.ld = self.im.load()
        self.getPrice()
        
    
    def getPrice(self):
        '''
        Function finds the paragraph containing electricity price

            Parameters:
                self : the object

        '''
        self.info = self.soup.find("p", class_ = 'h1 mb-0').text.split()
        self.priceNowTrondheim = float(self.info[5].replace(",","."))

    def getColorForPrice(self):
        '''
        Function that converts the current price to a corresponding rgb color 

        '''
        for x in range(self.im.size[0]):
            r, g, b = self.pixel(x, width=self.im.size[0], map=self.heatmap)
            r, g, b = [int(256*v) for v in (r, g, b)]
            for y in range(self.im.size[1]):
                self.ld[x, y] = r, g, b

        if(self.priceNowTrondheim > 3):
            self.red, self.green, self.blue = 255, 0, 0
        else:
            self.red, self.green, self.blue = self.ld[(int(999/3 * self.priceNowTrondheim),0)]
    
    def gaussian(self, x, a, b, c, d=0):
        return a * math.exp(-(x - b)**2 / (2 * c**2)) + d

    def pixel(self, x, width=100, map=[], spread=1):
        width = float(width)
        r = sum([self.gaussian(x, p[1][0], p[0] * width, width/(spread*len(map))) for p in map])
        g = sum([self.gaussian(x, p[1][1], p[0] * width, width/(spread*len(map))) for p in map])
        b = sum([self.gaussian(x, p[1][2], p[0] * width, width/(spread*len(map))) for p in map])
        return min(1.0, r), min(1.0, g), min(1.0, b)
    
    def saveCurrentPhoto(self):
        self.im.save("Regular_Webscraper/Gradient.png")


test = CurrentElectricityPriceTrondheim()
test.getColorForPrice()
print(test.red, " ", test.green, " ", test.blue)