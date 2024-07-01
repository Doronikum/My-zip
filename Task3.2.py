'''
Выполняется:
-вывод в консоль всех корзин с товарами из https://fakestoreapi.com
-вывод корзин с товарами выбранного покупателя

!для себя: библиотека устанавливается  pip install requests

'''
import json
import requests
#запрос всех корзин
url1="https://fakestoreapi.com/carts"
response_cart=requests.get(url1).json()

#запрос списка покупателей
url2='https://fakestoreapi.com/users'
response_users=requests.get(url2).json()

#формирование списка userId покупателей у которых есть корзины
sp_user_carts=[]
for n_user in response_cart:
    sp_user_carts.append(n_user['userId'])
    #print(sp_user_carts)

#вывод всех корзин
def carts_all():
    #перебор id корзин и поиск соответствующих им userId пользователей для вывода имен владельцев корзин
    n_cart=1
    for cart in response_cart:
        if cart['id']==n_cart:
            user=cart['userId']
            for users in response_users:
                if users['id']==user:
                    print(f'\nКорзина {n_cart}, Владелец: фамилия - {users['name']["firstname"]}, имя - {users['name']["lastname"]}')
            print(f'Id: {cart['id']},\nId Покупателя: {cart['userId']},\nДата: {cart['date']}') 
            for k in range(len(cart['products'])):
                print(f'Продукт №{k+1} - название {cart['products'][k]['productId']}, качество - {cart['products'][k]['quantity']}')
                #print(f'Продукт №{n_produkt+1} - название {cart['products'][n_produkt]['productId']}, качество - {cart['products'][n_produkt]['quantity']}')
                #n_produkt+=1
    
        n_cart+=1
    print('____________________')    
    return

#запрос ID покупателя и вывод его корзин
def ouput_user():
    #вывод списка покупателей с userId для выбора интересующего
    print("Выберете номер покупателя из списка:")
    j_users=1
    for users in response_users:
        if users['id']==j_users:
            print(f'{j_users}. {users['name']["firstname"]} {users['name']["lastname"]}')
            j_users+=1
 
    print('____________________')
    return
#выбор корзин интересующего покупателя  
def carts_user(j_users):
    
    #запрос ID покупателя
    #проверка вхождения номера покупателя в диапазон базы   
    n=0
    for n_user in response_users:
        if n_user['id']>n:
            n=n_user['id']

    if j_users<0 or j_users>n:
        print('Выход за диапазон пользователей', n)
        print('____________________')
        return

    #проверка - есть ли у этого покупателя корзины

    if j_users  not in sp_user_carts:
        print('У этого покупателя нет корзин')
        print('____________________')
        return        


    #запрос корзин этого покупателя
    url3='https://fakestoreapi.com/carts/user/'
    response_user_number=requests.get(f'{url3}{j_users}').json()
    #обработка и вывод информации о корзинах этого покупателя
    for users in response_users:
        if users['id']==j_users:
            print(f'{j_users}. {users['name']["firstname"]} {users['name']["lastname"]}')

            for users in response_user_number:
                print(f'Id: {users['id']},\nId Покупателя: {users['userId']},\nДата: {users['date']}') 
                for n in range(len(users['products'])):
                    print(f'Продукт №{n+1} - название {users['products'][n]['productId']}, качество - {users['products'][n]['quantity']}')

    print('____________________')
    return

if input("Вывести все корзины покупателей? (да)") =='да':
    carts_all()

if input("Вывести корзину конкретного покупателя? (да)") =='да':
    ouput_user()
    j_users=int(input("Для просмотра корзин покупателей введите номер покупателяили выход - 0 "))
    if j_users!=0:
        #запрос ID покупателя
        while j_users !=0:
            carts_user(j_users)
            j_users=int(input("Для просмотра корзин других покупателей введите номер покупателя или выход - 0 "))
