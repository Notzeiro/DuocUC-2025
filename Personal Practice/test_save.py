def save_data():
    with open("data.txt", "w") as file:
        file.write("Hello world!\n")
        file.write("This is saved in a file!\n")

def read_data():
    with open("data.txt", "r") as file:
        print("File contents:")
        print(file.read())

save_data()
read_data()
