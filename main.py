import notes
import tuesHistory
import osborn
import sys
import time

def write():
    print("Press '1' to view Osborne 1's history. \n\
Press '2' to view BASIC's history. \n\
Press '3' to view TUES' history. \n\
Press '4' to view Game Boy's history. \n\
Press '5' to type your notes. \n\
If you want to exit the system\n\
just type 'q' or 'quit'")


def again(i, a):
    i = input("Error! Please, type again. \n")
    while i not in a:
        i = input("Error! Please, type again. \n")
    return i

def runMain():    
    a = ['1', '2', '3', '4', '5']
    i = input()
    if i == 'q' or i == 'quit':
        print("You'll leave the system in 3 seconds.")
        time.sleep(3)
        sys.exit()
    if i not in a:
        i = again(i, a)
    else:
        if i == '1':
            osborn.run()
            print()
            write()
        elif i == '2':
            a = open("Basic.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '3':
            tuesHistory.run()
            print()
            write()
        elif i == '4':
            a = open("GameBoy.txt", 'r')
            print(a.read(), '\n')
            write()
        else:
            notes.run()
            print()
            write()

write()
while True:
    runMain()
