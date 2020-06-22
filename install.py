import os

try:
    os.system("pip install tqdm")
    print("[+]  Успешно устоновлена библиотека tqdm!")
except:
    print("[-]  Произошла ошибка при устоновке библиотеки tqdm, необходимо устоновить её в ручную!")
    exit()
from tqdm import trange

for i in trange(5):
    os.system("cls")
    if i == 0:
        try:
            os.system("pip install keyboard")
            print("[+]  Успешно устоновлена библиотека keyboard!")
        except:
            print("[-]  Произошла ошибка при устоновке библиотеки keyboard, необходимо устоновить её в ручную!")
            exit()	    
    if i == 1:
        try:
            os.system("pip install datetime")
            print("[+]  Успешно устоновлена библиотека datetime!")
        except:
            print("[-]  Произошла ошибка при устоновке библиотеки datetime, необходимо устоновить её в ручную!")
            exit()
    if i == 2:
        try:
            os.system("pip install codecs")
            print("[+]  Успешно устоновлена библиотека codecs!")
        except:
            print("[-]  Произошла ошибка при устоновке библиотеки codecs, необходимо устоновить её в ручную!")
            exit()
    if i == 3:
        try:
            os.system("pip install colorama")
            print("[+]  Успешно устоновлена библиотека colorama!")
        except:
            print("[-]  Произошла ошибка при устоновке библиотеки colorama, необходимо устоновить её в ручную!")
            exit()
    if i == 4:
        try:
            os.system("pip install os")    
            print("[+]  Успешно устоновлена библиотека os!")
            os.system("cls")
            print("[+]  Все библиотеки успешно устоновлены, кейлоггер готов к работе!\n\n\n")
        except:
            print("[-]  Произошла ошибка при устоновке библиотеки os, необходимо устоновить её в ручную!")
            exit()
