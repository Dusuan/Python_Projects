import sys
import clipboard
import json

SAVED_DATA =  "clipboard.json"



# Funcioneeeees
def save_data(filepath, data): #Funcion para guardar lo que hay en el clipboard a una key en json
    with open(filepath, "w") as f:
        json.dump(data, f)



def load_data(filepath):  #Funcnion para leer lo que hay dentro del json
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}

def delete_data(key):  #Funcion para borrar keys  
    if key in data:
            data.pop(key)
            save_data(SAVED_DATA, data)
            print("Key: "+key+ " deleted")









# Correr el programa en la consola
if len(sys.argv) == 2:
    
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":

        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!!!")

    elif command == "load":

        key = input("Enter the key to load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard: ")
        else:
            print("Key doesnt exist")


    elif command == "list":
        print(data)
   
    elif command == "delete":
        key = input("Type the key to be deleted: ")
        delete_data(key)

    else:
        print("Not available command")

else:
    print("Only type one command")
 