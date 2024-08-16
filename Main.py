import sqlite3

input_message = """
What Do You Want To Do ? 
"s" => Show All Skills 
"a" => Add New Skill
"d" => Delete Skill
"u" => Update Skill Progress
"q" => Quit The App 
"""

def Show_Skills():
    try:
        # Connect To Database
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()

        # Fetch Data And Show Skills
        cr.execute("SELECT * FROM SKILLS")
        results = cr.fetchall()
        print("--------------------- All Skills ------------------------")
        for skill_name, skill_progress in results:
            print(f"Skill Name => {skill_name} | Skill Progress => {skill_progress}")
        print("---------------------------------------------------------")

    except sqlite3.Error as error:
        print(f"Error, Failed To Connect To Database: {error}")

    finally:
        if db:
            db.close()

def Add_Skill(skill_name):
    try:
        # Connect To Database
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()

        # Create Table If Not Exists
        cr.execute("CREATE TABLE IF NOT EXISTS SKILLS(name text, progress integer DEFAULT 0)")

        # Insert Data To Database
        cr.execute("INSERT INTO SKILLS(name) VALUES(?)", (skill_name,))

        # Commit Changes
        db.commit()
        print(f"Skill {skill_name} Added Successfully")

    except sqlite3.Error as error:
        print(f"Error, Database Problem: {error}")

    finally:
        if db:
            db.close()

def Delete_Skill(skill_name):
    try:
        # Connect To Database
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()

        # Delete Data
        cr.execute("DELETE FROM SKILLS WHERE name = ?", (skill_name,))

        # Commit Changes
        db.commit()
        print(f"Skill {skill_name} Removed Successfully")

    except sqlite3.Error as error:
        print(f"Error, Database Problem: {error}")

    finally:
        if db:
            db.close()

def Update_Skill(skill_name, new_progress):
    try:
        # Connect To Database
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()

        # Update Data
        cr.execute("UPDATE SKILLS SET progress = ? WHERE name = ?", (new_progress, skill_name))

        # Commit Changes
        db.commit()
        print(f"Skill Progress {skill_name} Updated Successfully, New Progress = {new_progress}")

    except sqlite3.Error as error:
        print(f"Error, Database Error: {error}")

    finally:
        if db:
            db.close()

def Switch(user_input):
    if user_input == 's':
        Show_Skills()

    elif user_input == 'a':
        rep = 'y'
        while rep == 'y':
            Add_Skill(input("Skill Name: "))
            rep = input("Do You Want To Add More (y/n)? : ")

    elif user_input == 'd':
        rep = 'y'
        while rep == 'y':
            Delete_Skill(input("Skill Name: "))
            rep = input("Do You Want To Delete More (y/n)? : ")

    elif user_input == 'u':
        rep = 'y'
        while rep == 'y':
            Update_Skill(input("Skill Name: "), input("New Progress: "))
            rep = input("Do You Want To Update More (y/n)? : ")

    else:
        print("Not Found")

def Main():
    user_input = input(input_message).strip()
    while user_input != "q":
        Switch(user_input)
        user_input = input(input_message).strip()
    print("Quitting the application...")

if __name__ == "__main__":
    Main()
