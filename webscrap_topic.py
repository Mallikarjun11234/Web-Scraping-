import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=samsung+galaxy+s24&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_5_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_5_0_na_na_na&as-pos=5&as-type=HISTORY&suggestionId=samsung+galaxy+s24&requestId=4d5a7dd7-ef0a-49d1-8432-2dd25e475163")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_='KzDlHZ')
#print(names)
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
#print(name)

prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
#print(price)

ratings=soup.find_all('div',class_='XQDdHH')
rating=[]
for i in ratings[0:10]:
    d=i.get_text()
    rating.append(d)
#print(rating)

storages=soup.find_all('div',class_='J+igdf')
storage=[]
for i in storages[0:10]:
    d=i.get_text()
    storage.append(d)
#print(storage)

features=soup.find_all('div',class_='XG4BRas')
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)
#print(feature)

images=soup.find_all('img',class_='DByuf4')
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
#print(image)

#Pandas are used to convert the extracteed data into a structred data

df = pandas.DataFrame()
#print(df)
data = {'names':pandas.Series(name),
        'ratings':pandas.Series(rating),
        'prices':pandas.Series(price),
        'images':pandas.Series(image),
        'storages':pandas.Series(storage)}
df = pandas.DataFrame(data)
print(df)
df.to_csv("Mobiles_data.csv")