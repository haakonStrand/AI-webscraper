# AI-webscraper
The goal of the repo is to create a web scraper using AI (ChatGPT's API) and a webscraper using the beautifulSoup library

## Regular webscraper
The regular webscraper uses the beatifulSoup library. 
### Electricity price
The class `CurrentElectricityPriceTrondheim` is made to collect data from a website that displays the current electricity price in Trondheim.
This information is then parsed through a function that converts the price to a corresponding color.

The colorgradient used can be viewed in the figure below

![alt text](https://github.com/haakonStrand/AI-webscraper/blob/main/Regular_Webscraper/Gradient.png?raw=true)

The price ranges from zero (green on the left) to three (red on the right), If the price is above three NOK, the color will be red.
NB! All prices for this code is in Norwegian Krone.

#### Code usage
```
electricityPrice = CurrentElectricityPriceTrondheim()

electricityPrice.getColorForPrice()
```
After running the `electricityPrice.getColorForPrice()` function, you will be able to get the rgb values by calling the `getRGB()` function

```
RGB_color = getRGB() # Returns a tuple containing rgb values (red,green,blue)
```
