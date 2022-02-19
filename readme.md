# Install packages and requirements

pip pyinstaller

# To create exe, Open powershell terminal

pyinstaller -F -i "icon.ico" -n "Record Commander" RecordCommander.py --windowed

# First Time Use

    1 Ensure that .exe is located in folder where you plan on storing / reading your record.txt file
    2 Open Streamlabs and Record Commander
    3 Create a new Text (GDI+) source and make sure to select "Read from file"
    4 Click browse and select "record.txt"
    5 Place where needed and enjoy!

# How To use

    1 Always make sure that Record Commander is open when streaming
    2 When first opened, it will rewrite / create record.txt and set to "Record 0-0"
    3 Adjust your record by clicking the buttons in Record Commander and record.txt will update to reflect your new record
        - Please note, there is a slight delay (~1-2 seconds) between incrementing in Record Commander and Streamlabs reading the updated file

# Future updates

    - Make UI more pleasing
    - Implement keybinds for increments/decrements
    - Allow keybinds to be customized

## Current Version 0.1.1
