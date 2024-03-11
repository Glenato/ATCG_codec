#This python programme is just here to write text I do not what to write

#sudo python3 /Users/yannisjirsa/Desktop/2nd_A/ATCG/Codec/text-script.py

import keyboard
from time import sleep
from random import randint

text = "ATCG une entreprise révolutionnaire pour un nouveau système de stockage à la pointe de la tachnologie. Une capsule, un lecteur et un logiciel sont inclus et ce à des prix toujours plus compétitifs. Retrouvez aussi notre game de stockage en ligne sur notre site web : atcgfrench.wixsite/home"

a= True
while a==True: 
    if keyboard.is_pressed("space"):
        keyboard.press_and_release("backspace")
        a=False
        for i in range (len(text)):
            r = randint(1,3)
            sleep(r/1000)
            if text[i] in (".", ",", ":", "/"):
                if text[i] ==".":
                    keyboard.press_and_release('shift+'+";")
                elif text[i] =="/":
                    keyboard.press_and_release('shift+'+":")
                elif text[i] ==":":
                    keyboard.press_and_release(":")
                
            elif text[i].isupper():
                keyboard.press_and_release('shift+'+text[i])
            else:
                keyboard.press_and_release(text[i])
    

