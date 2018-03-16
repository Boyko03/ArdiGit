iimport sys
import time
import json

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


print("Hello! This is your note sheet. You can add your notes here. \n If you type 'q' or 'quit' you will exit the program \n \
and if you type 's' or 'search' you can find your notes by a keyword.")   
array_notes = []
text = input()
if text == "quit" or text == "q":
    array_format(array_notes)
    time.sleep(2)
    sys.exit()
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
	
time.sleep(len(array_notes))
sys.exit()
