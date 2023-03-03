# Synchronization of two folders 

## Overview

This Python script helps in synchronizing files between two folders and ensures that the replica folder exists.

### How to use

1. Install Python 3.x on your computer if you haven't already done.
2. Open a text editor such as Visual Studio Code.
3. Copy and paste the code above into the text editor.
4. Save the file as ***sync_folders.py***.
5. Open a terminal window and navigate to the directory where the ***sync_folders.py*** file is saved.
6. Type ***python sync_folders.py*** to run the script.
7. Follow the prompts to input the path to the source folder, replica folder, and log file.

### Functionality

This script synchronizes the files between two folders by copying newer files from the source to the replica folder. The script also checks for deleted files in the source folder and deletes them from the replica folder. Additionally, the script logs all events to a specified log file.

### Libraries used

> **os**: for interacting with the operating system.

> **shutil**: for high-level file operations.

> **time**: for getting the current time.

### Function Documentation

> **sync_folders(source_folder, replica_folder, log_file)** 
 
 This function synchronizes the files between two folders, the source folder and the replica folder. It also checks if the source and replica folders exist and creates the replica folder if it doesn't exist.

- **source_folder** (string): path to the source folder.
- **replica_folder** (string): path to the replica folder.
- **log_file** (string): path to the log file.

> **log(log_file, message)** 

This function logs the message to a file with a timestamp.

- **log_file** (string): path to the log file.
- **message** (string): message to log.

### Note

- The script will continuously run and check for changes every second until interrupted with CTRL + C.
- Make sure the paths to the source folder, replica folder, and log file are correct and exist before running the script.
- The log file will be created if it doesn't exist.
