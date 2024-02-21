import re
import uuid
from datetime import datetime as dt


id = 0
while True:
    command = input('Введите команду: ')

    if command == 'add' :
        i = 0
        title = input('Введите заголовок новой заметки: ')
        reader = open('notes.csv','r', encoding='UTF-8')
        for line in reader:
            a = re.split(';| ', line)
            if a[6] == title:
                print("такая заметка уже есть")
                i = 1
                break
        if i == 0:
            reader.close
            body = input('Введите тело новой заметки: ')
            data = open('notes.csv','a', encoding='UTF-8')
            id =  uuid.uuid4()
            data.write('id = ' + str(id) + '; заголовок = ' + title + '; тело = ' + body + "; " + dt.now().strftime('дата: %d.%m.%y время: %H:%M \n'))
            data.close()
            print('Заметка успешно сохранена')

    elif command == 'read':
        command = input('Что хотите вывести? \n')
        if (command == 'all') :
            data = open('notes.csv','r', encoding='UTF-8')
            for line in data:
                print(line)
            data.close()
        elif (command == 'date'):
            date = input('введите нужную дату: ')
            data = open('notes.csv','r', encoding='UTF-8')
            for line in data:
                a = re.split(';| ', line)
                for el in a:
                    if el == date:
                        print(line)
            data.close()
        elif (command == 'title'):
            i = 0
            title = input('введите нужный заголовок: ')
            data = open('notes.csv','r', encoding='UTF-8')
            for line in data:
                a = re.split(';| ', line)
                if a[6] == title:
                    print(line)
                    i = 1
            if i == 0:
                print('Заметка с таким заголовком не найдена')
            data.close()

        
    elif command == 'delete':
        res = []
        reader = open('notes.csv','r', encoding='UTF-8')
        title = input('Введите заголовок удаляемой заметки заметки: ')
        i = 0
        for line in reader:
            a = re.split(';| ', line)
            if a[6] != title:
                res += line
            else:
                i = 1
        if i == 0:
            print('Заметка не найдена')
        else:
            print('Заметка удалена')
        writer = open('notes.csv','w', encoding='UTF-8')
        for el in res:
            writer.write(el)
        reader.close()
        writer.close()

    elif command == 'redact':
        b = 0
        res = []
        reader = open('notes.csv','r', encoding='UTF-8')
        title = input('Введите заголовок редактируемой заметки: ')
        for line in reader:
            a = re.split(';| ', line)
            if a[6] == title:
                b = 1
                body = input('Введите новое тело заметки: ')
                line = 'id = ' + a[2] + '; заголовок = ' + title + '; тело = ' + body + "; " + dt.now().strftime('дата: %d.%m.%y, время: %H:%M \n')
                print('Заметка успешно сохранена')
            res += line
        if b == 0:
                print('Заметка не найдена')
        writer = open('notes.csv','w', encoding='UTF-8')
        for el in res:
            writer.write(el)
        reader.close()
        writer.close()

    elif (command == 'exit'):
        break


        

