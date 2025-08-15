from bs4 import BeautifulSoup as soup

import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get("https://books.toscrape.com/")

soupp = soup(response.text, 'html.parser')

testall = soupp.find('ul', class_='nav nav-list').find('li').find('ul')

categoryList = []
quantityList = []

i = 2

for li in testall.find_all('li'):
    # print(li.find('a').contents[0].strip())
    cat = li.find('a').contents[0].strip()
    categoryList.append(cat)

    url = 'https://books.toscrape.com/catalogue/category/books/' +  cat.replace(" ", "-").lower() + '_' + str(i) + '/index.html'

    response1 = requests.get(url)

    quantityAll = soup(response1.text, 'html.parser').find('form', class_='form-horizontal').find('strong')

    quantity = quantityAll.text
    quantityList.append(int(quantity))
    i = i+1

data_zipped = list(zip(categoryList, quantityList))
df = pd.DataFrame(data_zipped, columns=['Category', 'Quantity'])
df1 = df.head(10)

grafico = df1.plot(x='Category', y='Quantity', color='blue', kind='bar')
grafico.grid(zorder=0)
grafico.bar(categoryList, quantityList, color='blue', zorder=3)

plt.figure(figsize=(20, 3))


grafico.set_title("Quantidade de livros das 10 maiores categorias")
grafico.set_xlabel("Categorias")
grafico.set_ylabel("Quantidade")

plt.show()


