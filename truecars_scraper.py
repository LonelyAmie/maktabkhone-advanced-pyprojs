import requests as req
from bs4 import BeautifulSoup as bs
import re
import mysql.connector


model = input('what car: ')
url_text = req.get(f'https://www.truecar.com/used-cars-for-sale/listings/{model}/').text

soup = bs(url_text, 'html.parser')

my_cars = []

cnx = mysql.connector.connect(user = 'root', password = '1234', host = 'localhost', db = 'CAR_DATA')


print(len(soup.find_all('li', class_ = 'mt-3 flex grow col-md-6 col-xl-4')))


for car in soup.find_all('li', class_ = 'mt-3 flex grow col-md-6 col-xl-4') :
    name = car.find('span', class_ = 'truncate').text
    
    price = car.find('div' , class_ = 'heading-3 my-1 font-bold').text
    price = int(re.sub(r'\$(\d+),(\d+)$', '\g<1>\g<2>', price))
    
    milege = car.find('div', {'class': 'truncate text-xs', 'data-test' : 'vehicleMileage'}).text
    milege = int(re.sub(r'(\d*),(\d+) miles','\g<1>\g<2>', milege))
    
    data = (name, price, milege)
    my_cars.append(data)
    if len(my_cars) == 20 :
        break
    
with cnx.cursor() as cursor : 
    for car in my_cars :
        # query = 'INSERT INTO data VALUES (%s,%s,%s);', (car[0], car[1], car[2])
        
        # print('INSERT INTO data VALUES (%s,%s,%s);'('amir', 'khar', 'kir'))
        cursor.execute('INSERT INTO data VALUES (%s,%s,%s);', (car[0][:15], car[1], car[2]))
        cnx.commit()
    
    

   
    
    
