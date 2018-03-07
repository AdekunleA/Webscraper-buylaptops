import requests
from bs4 import BeautifulSoup as soup
f = open('BuyLaptops.csv','w')
headers = "Product,Description,Price\n"
f.write(headers)

page = requests.get ('http://www.buylaptopsinnigeria.com')

overall = soup(page.content,'html.parser')

names = overall.find_all('div',class_='image')

descriptions = overall.find_all('div',class_='opis')

prices = overall.find_all('div',class_='price')

intab = '₦'
outtab = 'N'
transtab = str.maketrans(intab,outtab)

for name,description,price in zip(names,descriptions,prices):
    Product = name.img['alt']
    fanta = description.text.strip()
    Description = fanta.replace(",","-")
    coke = price.text.strip()
    sprite = coke.translate(transtab)
    Price = sprite.replace(",","")
    f.write(Product + "," + Description + "," + Price + "\n")
        
    
    
    


f.close

