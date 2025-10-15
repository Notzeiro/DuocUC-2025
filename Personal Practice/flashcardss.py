import sys, time , keyboard , os

def typewriter_effect(text, delay=0.05): 
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char) # Write the character to the console
        sys.stdout.flush()     # Force the output to be displayed immediately
        time.sleep(delay)      # Pause for a short duration
    print() # Add a newline after the text is fully printed



class Flashcard:
    def __init__(self , title , question , content , group , id):
        self.title=title
        self.question=question
        self.content=content
        self.group=group
        self.id=id

    @staticmethod
    def create_flashcard():
        
        title=ask(typewriter_effect("Enter flashcard title: "))  
        question=ask(typewriter_effect("Question for the flashcard:"))
        content=ask("Enter flashcard content: ")
        group=ask("Assign a group to the flashcard (CASE SENSITIVE): ")

        id=(flashcards[-1])+1
        return Flashcard(title , question ,content , group , id)

    def show_flashcard(fc):
        typewriter_effect(f"Group:{fc.group}")
        typewriter_effect(fc.title)
        typewriter_effect(f'\n{fc.question}')
        time.sleep(3)
        typewriter_effect("Press enter to show the answer")
        keyboard.wait('enter')
        typewriter_effect(fc.content)


        



flashcards=[]

flashcards.append(Flashcard("test flashcard" , 'what is 2+2?' , "4", 'math' , 1))
flashcards.append(Flashcard("Chilenitos" , 'Cuales son los 3 ingredientes de los chilenitos?' , "Manteca, huevo, azucar flor", 'Cocina' , 2))
flashcards.append(Flashcard("Java Arraylists" , 'how do you initialize an ArrayList?' , "ArrayList<datatype> ListName = new ArrayList()", 'Python' , 3))


def simulate_loading(before_loading_text=2.5 , after_loading_text=2.5):
    time.sleep(before_loading_text)
    typewriter_effect("Loading..." , 0.05)
    time.sleep(after_loading_text)
    os.system("cls")


def ask(message):
    while True:
        variable=input(message)
        if variable:
            return variable
        print("cannot be empty")
   

def fc_by_group():
    typewriter_effect('||     TITLE     ||     GROUP     ||     ID     ||' , 0.01)
    for fc in flashcards:
        
        typewriter_effect(f'{fc.title}      {fc.group}       {fc.id}' , 0.01)
    typewriter_effect('Choose a group: ')
    choice=input()
    group_found=False
    for fc in flashcards:
        counter=1
        if fc.group==choice:
            group_found=True
            typewriter_effect(f"Flashcards seen:{counter}")
            Flashcard.show_flashcard(fc)
            counter+=1
    if not group_found:
        typewriter_effect("Group not found")

def fc_by_id():
    typewriter_effect('||     TITLE     ||     GROUP     ||     ID     ||' , 0.01)
    for fc in flashcards:
        typewriter_effect(f'{fc.title}      {fc.group}       {fc.id}' , 0.01)
    typewriter_effect('Enter ID: ')
    choice=input()
    for fc in flashcards:
        if fc.id==choice:
            id_found=True
            Flashcard.show_flashcard(fc)
        else:
            typewriter_effect("Incorrect flashcard id")


def option_one(): #STUDY FLASHCARDS
    print("\n--- Option 1 Selected ---")
    simulate_loading()
    typewriter_effect("Flashcard selection \n1.-Select by id (one only)\n2.-Select by group(multiple)\n3.-Back to main menu")
    choice=input("Option (1-3):")
    match choice:
        case "1":
            fc_by_id()
        case "2":
            fc_by_group()
        case "3":
            return
        case _:
            typewriter_effect("Option not valid")

    
            

def option_two(): #CREATE FLASHCARDS
    print("\n--- Option 2 Selected ---")


def option_three():
    print("\n--- Option 3 Selected ---")
   
def quit_program():
    print("\n--- Thank you for using the program! Goodbye! ---")
    sys.exit(0)

def display_menu():
    os.system("cls")
    print("====================================")
    print("          MAIN MENU CHOICES         ")
    print("====================================")
    print("1. Study")
    print("2. Create and modify flashcards")
    print("3. Settings")
    print("4. Exit Program")
    print("------------------------------------")

def main():
    menu_options = {
        '1': option_one,
        '2': option_two,
        '3': option_three,
        '4': quit_program
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice in menu_options:
            menu_options[choice]()
        else:
            typewriter_effect(f"\n[ERROR]: Invalid choice '{choice}'.\n")
            input()
            

main()
