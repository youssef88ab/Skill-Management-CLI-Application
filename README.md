# Skill Management CLI Application

A command-line application for managing and tracking skills using an SQLite database. This tool allows users to add, delete, update, and view skills along with their progress.

## Features

- **Show All Skills**: Display a list of all skills and their current progress.
- **Add New Skill**: Add a new skill to the database.
- **Delete Skill**: Remove a skill from the database.
- **Update Skill Progress**: Modify the progress of an existing skill.
- **Quit Application**: Exit the application.

## Installation

### Prerequisites

- Python 3.x
- SQLite (comes bundled with Python)

### Steps to Install

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/skill-management-cli.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd skill-management-cli
    ```

3. **Install Required Packages**

    No additional packages are required beyond Python and SQLite.

## Usage

1. **Run the Application**

    Execute the following command to start the application:

    ```bash
    python skill_management.py
    ```

2. **Command Options**

    The application will prompt you with the following options:

    - **"s"**: Show all skills.
    - **"a"**: Add a new skill.
    - **"d"**: Delete an existing skill.
    - **"u"**: Update the progress of a skill.
    - **"q"**: Quit the application.

3. **Examples**

    - **Adding a New Skill**

      ```
      a
      Skill Name: Python
      Do You Want To Add More (y/n)? : n
      ```

    - **Updating Skill Progress**

      ```
      u
      Skill Name: Python
      New Progress: 75
      Do You Want To Update More (y/n)? : n
      ```

    - **Deleting a Skill**

      ```
      d
      Skill Name: Python
      Do You Want To Delete More (y/n)? : n
      ```

## Code Overview

- **`Show_Skills()`**: Connects to the SQLite database, retrieves all skills, and displays them.
- **`Add_Skill(skill_name)`**: Adds a new skill to the database.
- **`Delete_Skill(skill_name)`**: Deletes a skill from the database.
- **`Update_Skill(skill_name, new_progress)`**: Updates the progress of a specified skill.
- **`Switch(user_input)`**: Directs user input to the appropriate function.
- **`Main()`**: Runs the main loop of the application, allowing user interaction.
