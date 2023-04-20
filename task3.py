#оффлайн чат-бот

import json

with open('bot.json', encoding='utf-8') as data:
    text = json.load(data)
flag = True
while flag:
    q = input('Ожидаю вопроса... ').lower()
    if q.lower().startswith('стоп') or q.lower().startswith('пока'):
        break
    if q not in text.keys():
        print('К сожалению такой информации пока нет в моей библиотеке. Давайте попробуем еще :)')
    else: print(text[q])
