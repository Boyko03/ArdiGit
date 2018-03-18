import sys
import time
import json
import os

def write():
    print("Press '1' to view Osborne 1's history. \n\
Press '2' to view BASIC's history. \n\
Press '3' to view TUES' history. \n\
Press '4' to view Game Boy's history. \n\
Press '5' to type your notes. \n")


def again(i, a):
    i = input("Error! Please, type again. \n")
    while i not in a:
        i = input("Error! Please, type again. \n")
    return i

def run():    
    a = ['1', '2', '3', '4', '5', '6']
    i = input()
    if i not in a:
        i = again(i, a)
    else:
        if i == '1':
            a = open("Osborn1.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '2':
            a = open("BASIC.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '3':
            a = open("TUES.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '4':
            a = open("GameBoy.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '5':
            note()
            write()
        elif i == '6':
            time.sleep(1)
            sys.exit()

def note():
    array_notes = []

    if os.stat("file.json").st_size != 0:
        yesNo = input("You have already made some notes. Do you want to continue writting? Yes/No: ")
        if yesNo == "yes":
            with open('file.json') as file:
                array_notes = json.loads(file.read())

    def array_format(array):
        for i in range(len(array)):
            format_string(array[i])

    def format_string(string):
        a1 = str(string)
        a1 = a1.strip()
        a1 = a1.replace("[", "")
        a1 = a1.replace("]", "")
        a1 = a1.replace("'", "")
        a1 = a1.replace("\t", "")
        print(a1)
        
    def search(text, array):
        text = input("Search for: ")
        count = 0
        for i in array:
            if text in i:
                format_string(i)
                count += 1
        if count == 0:
            print("The object was not found. ")


    print("\n Hello! This is your note sheet. You can add your notes here. \n If you type 'q' or 'quit' you will exit the program \n \
and if you type 's' or 'search' you can find your notes by a keyword. \n")   

    text = input()
    if text == "quit" or text == "q":
        array_format(array_notes)
        time.sleep(2)
        return
    elif text == "search" or text == "s":
        search(text, array_notes)
    else:
        array_notes.append(text)

    while text != "quit" or text != "q":
        text = input()
        if text == "quit" or text == "q":
            break
        elif text == "search" or text == "s":
            search(text, array_notes)
        else:
            array_notes.append(text)   

    array_format(array_notes)

    with open('file.json', 'w') as file:
            file.write(json.dumps(array_notes))
            
    time.sleep(3)
    return
    
write()
while True:
    run()
