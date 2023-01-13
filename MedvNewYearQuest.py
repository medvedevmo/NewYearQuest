# Вам нужно загрузить BeautifulSoup и requests!
# pip install beautifulsoup4
# pip install requests
from bs4 import BeautifulSoup
import requests
# Начало
print('Начало игры.')
print('Вы являетесь дедом морозом. Вам нужно набрать как можно большую скорость для ваших санок')
print('Санки поломаны. Починить или собрать новые?')
answer = input().lower()
while answer != 'починить' and answer != 'собрать новые':
    print('Неверный ответ')
    answer = input().lower()
if answer == 'починить':
    print('Что починить, передний физюляж или ОДК?')
    answer = input().lower()
    while answer != 'одк' and answer != 'физюляж':
        print('Неверный ответ')
        answer = input().lower()
    if answer == 'одк':
        print('У санок санты нету ОДК.\nПопробуйте снова')
        exit()
    elif answer == 'физюляж':
        print('На ремонт физюляжа нужно 5кг алюминия.\nЧто лучше купить, 8кг со скидкой 20% и ценой 1300 за кг или 6кг со скидкой 10% и ценой 1450 за кг?\nВведите цифру ответа (1 или 2)')
        answer = input()
        while answer != '1' and answer != '2':
            print('Неверный ответ')
            answer = input()
        if answer == '1':
            print('Верно!')
        else:
            print('Попробуйте снова')
            exit()
elif answer == 'собрать новые':
    print('Какого материала сделать санки: невесомого, или из дерева, металла, пластика?')
    answer = input().lower()
    while 'невесом' not in answer and not ('дерев' in answer and 'металл' in answer and 'пластик' in answer):
        print('Неверный ответ')
        answer = input().lower()
    if 'невесом' in answer:
        print('Поздравляем, новые санки пригодны')
    else:
        print('К сожалению санки не взлетят.\nПопробуйте снова')
        exit()
print('Сколько подарков нужно на каждого человека?\nДанные брать с сайта https://gtmarket.ru/ratings/world-population')
answer = int(input())

url = 'https://gtmarket.ru/ratings/world-population'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
getParsed = int(soup.findAll('td', class_='nobr')[0].text.replace(" ", ""))
print('Данные с сайта:', getParsed)
if getParsed == answer:
    print('Поздравляем, правильный ответ!')
else:
    print('Попробуйте снова')
