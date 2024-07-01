import requests
print('hello')
#n=189002913 #376413651 5949098925
# app=51970284

login=int(input("Введите Ваш ID VK"))
token=str(input("Введите Ваш ключ в VK"))
login_user=input("Введите ID VK интересного клиента VK")
'''это мои данные
login=5949098925
token='vk1.a.keGeRl0744nFvOzyMGQkjKPEPe5hwcuzpnl3uvYp1atvzgMJTK6uArefknbSFfMSPn6V8gB_EFTi2tVZ8ZLCALT_Rzoz4KOPO5zOurdW2Ew0oec-_GXnSROM0VDFhiBuJ5QUK3qeCqqx2hP9Gr7drfp0poxThBcyigikuckZDdkQ_NZ9c8539O1IhM0x3AZ73wYbceUZgsQY7qF1DiT8ig'
login_user=189002913
'''
#разрезаю url на части.
#url='https://api.vk.com/method/friends.get?user_id=189002913&order=hints&access_token=vk1.a.keGeRl0744nFvOzyMGQkjKPEPe5hwcuzpnl3uvYp1atvzgMJTK6uArefknbSFfMSPn6V8gB_EFTi2tVZ8ZLCALT_Rzoz4KOPO5zOurdW2Ew0oec-_GXnSROM0VDFhiBuJ5QUK3qeCqqx2hP9Gr7drfp0poxThBcyigikuckZDdkQ_NZ9c8539O1IhM0x3AZ73wYbceUZgsQY7qF1DiT8ig&v=5.199'
url1_1='https://api.vk.com/method/friends.get?user_id='
#vk1.a.keGeRl0744nFvOzyMGQkjKPEPe5hwcuzpnl3uvYp1atvzgMJTK6uArefknbSFfMSPn6V8gB_EFTi2tVZ8ZLCALT_Rzoz4KOPO5zOurdW2Ew0oec-_GXnSROM0VDFhiBuJ5QUK3qeCqqx2hP9Gr7drfp0poxThBcyigikuckZDdkQ_NZ9c8539O1IhM0x3AZ73wYbceUZgsQY7qF1DiT8ig
url1_2='&order=hints&access_token='
url1='https://api.vk.com/method/users.get?user_id='
url2='&fields=bdate&access_token='
url3='&v=5.199'
#Вывод количества друзей у login_user
response=requests.get(f'{url1_1}{login_user}{url1_2}{token}{url3}')
print(response.status_code)
user_info = response.json()["response"]
friends=[]
for i in user_info['items']:
        friends.append(i)
n_friends=user_info['count']
print(f"У пользователя VK имеющего ID= Число друзей = {n_friends}")
#Запрос операций с login_user
#ВНИМАНИЕ!!! Выбор  3-перечислить профили друзей уверенно работает когда запросим не более 9 друзей за 1 раз
vvod=int(input('Что вывести: 1-список ID друзей, 2-вывод профиля конкретного друга, 3-перечислить профили друзей, 0 - выход'))
while vvod!=0:   
    if vvod==1:
        #вывод ID по введенному login_user
        print(f"Список друзей = {friends}")
    elif vvod==2:
        n_fr=input("Введите ID друга")
        response=requests.get(f'{url1}{n_fr}{url2}{token}{url3}')
        friend_info = response.json()["response"][0]
        bdate_new="Не указан"   
        try:
             bdate_new=friend_info['bdate']
        except KeyError:
           pass
        print(f'{n_fr}. Имя {friend_info['first_name']}, фамилия {friend_info['last_name']}, день рождения {bdate_new}')     
    elif vvod==3:
        #вывод перечня друзей
        print("Вывод профилей друзей")
        vvod_min=int(input("Введите Минимальный номер друга в списке"))
        vvod_max=int(input("Введите Максимальный номер друга в списке. Рекомендовано выводить не более 9 друзей за раз."))
        i=vvod_min-1
        while vvod!=0:  
            response=requests.get(f'{url1}{friends[i]}{url2}{token}{url3}')
            friend_info = response.json()["response"][0]
            bdate_new="Не указан"
            try:
                #if friend_info['bdate']==None:
               bdate_new=friend_info['bdate']
            except KeyError:
                pass
            print(f'{i+1}. ID={friends[i]} {friend_info['first_name']} {friend_info['last_name']}, день рождения {bdate_new}')
            #vvod=input("Следующий друг-ENTER. Если СТОП введите-0")
            i+=1
            if i==n_friends or i==vvod_max:
                pass
                vvod_min=int(input("Введите Минимальный номер друга в списке или 0 - выход"))
                vvod_max=input("Введите Максимальный номер друга в списке или 0 - выход. Рекомендовано выводить не более 9 друзей за раз.")
                vvod_max=int(vvod_max)  
                i=vvod_min-1              
                if vvod_min==0 or vvod_max==0:
                    vvod=0
                    
            else:
                pass


    vvod=int(input('Что вывести: 1-список ID друзей, 2-вывод профиля конкретного друга, 3-перечислить профили друзей, 0 - выход'))
            #vvod=0 
