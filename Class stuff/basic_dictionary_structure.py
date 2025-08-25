dictionary_example={1: {"data1": "JohnPork", "data2": True, "data3": "ABC123"},
                    2: {"data1": "Peepo", "data2": False, "data3": "XYZ789"},
                    3: {"data1": "Jiwooves", "data2": True, "data3": "LMN456"}}

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
        print()

def add_entry(dictionary):
    last_key = (dictionary.keys()[-1]) 
    key=last_key + 1 if last_key is not None else 1
    data1 = input("Enter data1: ")
    data2 = input("Enter data2: ")
    data3 = input("Enter data3: ")
    dictionary[key] = {"data1": data1, "data2": data2, "data3": data3}

def remove_entry(dictionary):
    try:
        print_dictionary(dictionary)
        key = int(input("Enter the key of the entry to remove: "))
        if key in dictionary:
            del dictionary[key]
            print(f"Entry with key {key} removed.")
        else:
            print(f"No entry found with key {key}.")
    except ValueError:
        print("Invalid input. Please enter a valid key.")

def edit_entry(dictionary):
    try:
        print_dictionary(dictionary)
        key = int(input("Enter the key of the entry to edit: "))
        if key in dictionary:
            data1 = input("Enter new data1 (leave blank to keep current): ")
            data2 = input("Enter new data2 (leave blank to keep current): ")
            data3 = input("Enter new data3 (leave blank to keep current): ")
            if data1:
                dictionary[key]["data1"] = data1
            if data2:
                dictionary[key]["data2"] = data2
            if data3:
                dictionary[key]["data3"] = data3
            print(f"Entry with key {key} updated.")
        else:
            print(f"No entry found with key {key}.")
    except ValueError:
        print("Invalid input. Please enter a valid key.")




