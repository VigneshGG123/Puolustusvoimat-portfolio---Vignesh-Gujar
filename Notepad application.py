def create_new_note():
    folder_path = 'notes'
    file_name = input("Enter the filename (with extension): ")
    file_path = f"{folder_path}/{file_name}"
    content = input("Enter the content to be saved in the file: ")

    with open(file_path, 'w') as file:
        file.write(content + "\n")
    print(f"File '{file_name}' saved to '{folder_path}'.")

def view_note(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"--- {file_path} ---\nContent:\n{content}\n{'-' * (len(file_path) + 8)}")
    except FileNotFoundError:
        print(f"Note with filename '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while viewing '{file_path}': {e}")

def updated_content(file_path, old_text, new_text):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        updated_content = content.replace(old_text, new_text)

        with open(file_path, 'w') as file:
            file.write(updated_content)

        print("Note was updated successfully")
    except FileNotFoundError:
        print(f"Note with filename '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while updating '{file_path}': {e}")

def edit_note(file_path):
    view_note(file_path)

    while True:
        print("1. Continue writing")
        print("2. Choose a highlighted area")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            updated_text = input("Enter updated content here: ")
            with open(file_path, "a") as file:
                file.write("\n" + updated_text)
            print("Content has been updated.")
        elif choice == "2":
            current_content = read_file_content(file_path)
            if current_content is not None:
                while True:
                    old_text_input = input("Write text you want to replace: ")
                    if old_text_input in current_content:
                        break
                    else:
                        print(f"Error: '{old_text_input}' not found in the note. Please enter a valid text.")
                new_text_input = input("Write new text: ")
                updated_content(file_path, old_text_input, new_text_input)
            else:
                print("Error reading the file content.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Note with filename '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")
    return None

def main():
    while True:
        print("\nNote-Making App Menu:")
        print("1. View a Note")
        print("2. Edit a Note")
        print("3. Create a Note")
        print("4. Exit")

        user_choice = input("Enter your choice (1-4): ")

        if user_choice == "1":
            note_name = input("Enter the name of the note: ")
            full_path = f"notes/{note_name}"
            view_note(full_path)
        elif user_choice == "2":
            note_name = input("Enter the name of the note: ")
            full_path = f"notes/{note_name}"
            edit_note(full_path)
        elif user_choice == "3":
            create_new_note()
            print("New note has been created")
        elif user_choice == "4":
            print("Exiting the Note-Making App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
