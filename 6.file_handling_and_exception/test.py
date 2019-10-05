def file_operator(file_name, mode):
    try:
        if mode == "r":
            with open(file_name, "r") as file:
                print(file.read())
        elif mode == "w":
            with open(file_name, "a") as file:
                file.write("New Content")
                file.close()
                file = open(file_name, "r")
                print(file.read())
    except IOError:
        print("Error")

def prompt():
    message = "Please input the file name: "
    file_name = input(message)
    message = "Read or Write?(r, w) "
    mode = input(message)
    file_operator(file_name, mode)
    
prompt()