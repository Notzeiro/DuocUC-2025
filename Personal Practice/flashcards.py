import json, os, time

DATA_FILE = 'flashcards_data.json'

class Flashcard:
    def __init__(self, flashcardTitle, flashcardContent):
        self.flashcardTitle = flashcardTitle
        self.flashcardContent = flashcardContent

    def to_dict(self):
        """Converts the Flashcard object to a dictionary for JSON saving."""
        return {
            'title': self.flashcardTitle,
            'content': self.flashcardContent
        }

    @staticmethod
    def from_dict(data):
        """Creates a Flashcard object from a dictionary loaded from JSON."""
        return Flashcard(data['title'], data['content'])

# --- 2. Persistence (Save/Load) ---

def load_data():
    """Loads all flashcards grouped by topic from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            # Convert dictionary back into Flashcard objects for use in the program
            for group, cards_list in data.items():
                data[group] = [Flashcard.from_dict(card_data) for card_data in cards_list]
            return data
    except json.JSONDecodeError:
        print(f"Error reading {DATA_FILE}. Starting with an empty set.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred during loading: {e}. Starting with an empty set.")
        return {}

def save_data(flashcard_groups):
    """Saves all flashcards (converted to dictionaries) to the JSON file."""
    # Convert Flashcard objects back to dictionaries for JSON saving
    data_to_save = {}
    for group, cards_list in flashcard_groups.items():
        data_to_save[group] = [card.to_dict() for card in cards_list]

    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data_to_save, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# --- 3. Core Functions ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_card(content_lines, flipped=False):
    """Visually draws the flashcard in the console."""
    card_width = 70
    border = "═" * card_width
    padding = " " * 2

    print("\n" + "╔" + border + "╗")
    
    # Print content lines
    for line in content_lines:
        display_line = line.ljust(card_width - len(padding) * 2)
        print(f"║{padding}{display_line}{padding}║")

    # Add separator line
    if flipped:
        print("║" + "=" * card_width + "║")
        print(f"║{'BACK - CONTENT REVEALED'.center(card_width)}║")
        print("║" + "=" * card_width + "║")
    else:
        print("║" + "-" * card_width + "║")
        print(f"║{'FRONT - Press ENTER to FLIP'.center(card_width)}║")
        print("║" + "-" * card_width + "║")


    # Calculate remaining empty space
    # Ensures the card has a minimum height for better visual appeal
    min_height = 8
    current_height = len(content_lines) + 4 # 4 lines for separators/instructions
    
    for _ in range(max(0, min_height - current_height)):
        print(f"║{''.ljust(card_width)}║")

    print("╚" + border + "╝")


def study_group(flashcard_groups, group_name):
    """Iterates through flashcards in a group for studying."""
    if group_name not in flashcard_groups or not flashcard_groups[group_name]:
        print("No cards found in this group.")
        time.sleep(2)
        return

    cards = flashcard_groups[group_name]
    card_count = len(cards)
    
    for i, card in enumerate(cards):
        # 1. Show the Front (Title)
        clear_screen()
        print(f"\n--- STUDYING: {group_name} ({i + 1}/{card_count}) ---\n")
        
        # Split the title for visual display
        title_lines = [f"TITLE: {card.flashcardTitle}"]
        draw_card(title_lines, flipped=False)
        
        input("\nPress ENTER to flip the card and reveal the content...")

        # 2. Show the Back (Content)
        clear_screen()
        print(f"\n--- STUDYING: {group_name} ({i + 1}/{card_count}) ---\n")
        
        # Combine title and content for flipped view
        content_lines = [
            f"QUESTION/TITLE:",
            f"{card.flashcardTitle}",
            "", # Spacer
            f"ANSWER/CONTENT:",
            f"{card.flashcardContent}"
        ]
        draw_card(content_lines, flipped=True)

        # Decide whether to continue or exit
        if i < card_count - 1:
            input("\nPress ENTER to continue to the next card...")
        else:
            input("\nThat was the last card! Press ENTER to return to the main menu...")

def create_flashcard(flashcard_groups):
    """Allows the user to create a new flashcard and assign it to a group."""
    clear_screen()
    print("\n--- CREATE NEW FLASHCARD ---\n")
    
    # Get card details
    title = input("Enter the FLASHCARD TITLE (Front of card): ").strip()
    if not title:
        print("Title cannot be empty. Creation cancelled.")
        time.sleep(1.5)
        return
        
    content = input("Enter the FLASHCARD CONTENT (Back of card): ").strip()
    if not content:
        print("Content cannot be empty. Creation cancelled.")
        time.sleep(1.5)
        return

    # Select/Create Group
    print("\nAvailable Groups:")
    if flashcard_groups:
        for i, group in enumerate(flashcard_groups.keys()):
            print(f"  [{i+1}] {group}")
    
    new_group_name = input("\nEnter Group Name (type an existing name or a new name to create): ").strip()
    if not new_group_name:
        print("Group name cannot be empty. Creation cancelled.")
        time.sleep(1.5)
        return

    # Create the card object
    new_card = Flashcard(title, content)
    
    # Add to the group
    if new_group_name not in flashcard_groups:
        flashcard_groups[new_group_name] = []
        print(f"\nGroup '{new_group_name}' created!")

    flashcard_groups[new_group_name].append(new_card)
    save_data(flashcard_groups)
    print(f"\nSuccess! Flashcard saved to group '{new_group_name}'.")
    time.sleep(2)

def view_groups(flashcard_groups):
    """Displays a list of available groups and prompts the user to select one to study."""
    if not flashcard_groups:
        clear_screen()
        print("\n--- VIEW GROUPS ---\n")
        print("No flashcard groups found. Create one first!")
        input("\nPress ENTER to return to the main menu...")
        return

    while True:
        clear_screen()
        print("\n--- SELECT GROUP TO STUDY ---\n")
        groups = list(flashcard_groups.keys())
        
        for i, group in enumerate(groups):
            count = len(flashcard_groups[group])
            print(f"  [{i+1}] {group} ({count} cards)")
        
        print("\n  [R] Return to main menu")
        
        choice = input("\nEnter number to study group or R to return: ").strip().lower()
        
        if choice == 'r':
            return
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(groups):
                study_group(flashcard_groups, groups[index])
                # After studying, loop back to group selection
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
        except ValueError:
            print("Invalid input. Please enter a number or 'R'.")
            time.sleep(1)

# --- 4. Main Application Loop ---

def main_menu():
    """The main entry point and loop for the application."""
    flashcard_groups = load_data()

    while True:
        clear_screen()
        print("=========================================================")
        print("             Simple Python Flashcard Manager             ")
        print("=========================================================")
        print("  [1] Create New Flashcard")
        print("  [2] View & Study Groups")
        print("  [3] Exit and Save")
        print("=========================================================")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            create_flashcard(flashcard_groups)
        elif choice == '2':
            view_groups(flashcard_groups)
        elif choice == '3':
            save_data(flashcard_groups)
            print("\nAll flashcards saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()