import sqlite3

input_message = """
What Do You Want To Do? 
"s" => Show All Skills 
"a" => Add New Skill
"d" => Delete Skill
"u" => Update Skill Progress
"q" => Quit The App 
"""

def create_table():
    try:
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()
        cr.execute("CREATE TABLE IF NOT EXISTS SKILLS(name text, progress integer DEFAULT 0)")
        db.commit()
    except sqlite3.Error as error:
        print(f"Error creating table: {error}")
    finally:
        if db:
            db.close()

def Show_Skills():
    try:
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()
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
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()
        cr.execute("INSERT INTO SKILLS(name) VALUES(?)", (skill_name,))
        db.commit()
        print(f"Skill {skill_name} Added Successfully")
    except sqlite3.Error as error:
        print(f"Error, Database Problem: {error}")
    finally:
        if db:
            db.close()

def Delete_Skill(skill_name):
    try:
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()
        cr.execute("DELETE FROM SKILLS WHERE name = ?", (skill_name,))
        db.commit()
        print(f"Skill {skill_name} Removed Successfully")
    except sqlite3.Error as error:
        print(f"Error, Database Problem: {error}")
    finally:
        if db:
            db.close()

def Update_Skill(skill_name, new_progress):
    try:
        db = sqlite3.connect("Skills.db")
        cr = db.cursor()
        cr.execute("UPDATE SKILLS SET progress = ? WHERE name = ?", (int(new_progress), skill_name))
        db.commit()
        print(f"Skill Progress {skill_name} Updated Successfully, New Progress = {new_progress}")
    except ValueError:
        print("Invalid input. Progress should be a number.")
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
        while rep.lower() == 'y':
            Add_Skill(input("Skill Name: ").strip())
            rep = input("Do You Want To Add More (y/n)? : ").strip()
    elif user_input == 'd':
        rep = 'y'
        while rep.lower() == 'y':
            Delete_Skill(input("Skill Name: ").strip())
            rep = input("Do You Want To Delete More (y/n)? : ").strip()
    elif user_input == 'u':
        rep = 'y'
        while rep.lower() == 'y':
            skill_name = input("Skill Name: ").strip()
            new_progress = input("New Progress: ").strip()
            Update_Skill(skill_name, new_progress)
            rep = input("Do You Want To Update More (y/n)? : ").strip()
    else:
        print("Option not recognized, please try again.")

def Main():
    create_table()  # Ensure table exists before starting
    user_input = input(input_message).strip()
    while user_input != "q":
        Switch(user_input)
        user_input = input(input_message).strip()
    print("Quitting the application...")

if __name__ == "__main__":
    Main()
