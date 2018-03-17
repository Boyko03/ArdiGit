def write():
    print("Press '1' to view Osborne 1's history. \n\
Press '2' to view BASIC's history. \n\
Press '3' to view TUES's history. \n\
Press '4' to view Game Boy's history. \n\
Press '5' to type your notes. \n")


def again(i, a):
    i = input("Error! Please, type again. \n")
    while i not in a:
        i = input("Error! Please, type again. \n")
    return i

def run():    
    a = ['1', '2', '3', '4', '5']
    i = input()
    if i not in a:
        i = again(i, a)
    else:
        if i == '1':
            a = open("Osborne1Article.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '2':
            a = open("Basic.txt", 'r')
            print(a.read(), '\n')
            write()
        elif i == '3':
            import tuesHistory
            print()
            write()
        elif i == '4':
            a = open("GameBoy.txt", 'r')
            print(a.read(), '\n')
            write()
        else:
            import notes
            write()

write()
while True:
    run()
