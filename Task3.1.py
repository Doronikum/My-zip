'''
вывод в консоль категории и информации о товарах из https://fakestoreapi.com

для себя: библиотека устанавливается  pip install requests

'''
import json
import requests
url="https://fakestoreapi.com/products/categories"
response=requests.get(url).json()
#запрос категории товара
print('Имеющиеся категории товаров:')
j=0
for i in response:
    j=j+1
    print(f'{i}- категория {j}')

num=int(input('Выберете категорию товара:'))   
while num>j or num<1:
    print(f'Выберете категорию товара в диапазоне: 1-{j}')
    num=int(input('')) 
print(f'Товары категории {num}:')
j=0
for i in response:
    j+=1
    if j==num:
             
        url="https://fakestoreapi.com/products/category/"
        response=requests.get(f'{url}{i}').json()
        #print(f'{url}{i}')


j=0
for sl in response:
    if sl['id']!=0:
        j+=1
        print(f'{j}. {sl['title']} - товар {j}')

#запрос номера товара
num=int(input('Выберете номер товара:'))
while num>j or num<1:
    print(f'Выберете номер товара в диапазоне: 1-{j}')
    num=int(input('')) 
j=0
for sl in response:
    j+=1
    if num==j:
        print(f'Название: {sl['title']},\nАрт.: {sl['id']},\nЦена: {sl['price']},\nОписание: {sl['description']},\nРэйтинг: {sl['rating']['rate']} в {sl['rating']['count']} запросах')


                    
