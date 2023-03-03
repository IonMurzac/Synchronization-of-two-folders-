# Import necessary libraries
import os
import shutil
import time


def sync_folders(source_folder, replica_folder, log_file):
    """
    This Function synchronize the files between two folders, the source folder and the replica folder,
    and checks if the source and replica folders exist, creates the replica folder if it doesn't exist.
    It then synchronize the files between the folders, copying newer files from the source to the replica folder.
    Finally, it checks for deleted files in the source folder and deletes them.

    ->param src_folder: path to the source folder
    ->param replica_folder: path to the replica folder
    ->param log_file: path to the log file
    """
    while True:
        try:
            # Check if source folder exists, If the folder does not exist, an exception is 
            # raised with a message indicating that the folder does not exist. 
            if not os.path.exists(source_folder):
                raise Exception(f"{source_folder} does not exist")

            # Check if replica folder exists, if it doesn't exist, it creates it where indicated
            if not os.path.exists(replica_folder):
                os.makedirs(replica_folder)

            # Sync the folders
            for root, dirs, files in os.walk(source_folder):
                # Create path to the replica files from source files
                for filename in files:
                    source_file = os.path.join(root, filename)
                    replica_file = source_file.replace(source_folder, replica_folder, 1)

                    # Create a replica file for each source file
                    if not os.path.exists(replica_file) or os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                        # File doesn't exist or is newer in source folder, then copy the file to the replica folder 
                        shutil.copy2(source_file, replica_file)
                        log(log_file, f"copied {source_file} to {replica_file}")
                
                # Copy the directories from the source folder to the replica folder 
                for dirname in dirs:
                    source_dir = os.path.join(root, dirname)
                    replica_dir = source_dir.replace(source_folder, replica_folder, 1)

                    # Create a replica directory and write log message
                    if not os.path.exists(replica_dir):
                        os.makedirs(replica_dir)
                        log(log_file, f"created directory {replica_dir}")

            # Check for deleted files in destination folder
            for root, dirs, files in os.walk(replica_folder):
                for filename in files:
                    replica_file = os.path.join(root, filename)
                    source_file = replica_file.replace(replica_folder, source_folder, 1)

                    # If files doesn't exist in source folder, then it deletes them from the replica folder
                    if not os.path.exists(source_file):
                        os.remove(replica_file)
                        log(log_file, f"deleted {replica_file}")

                # Check all directories in both folders
                for dirname in dirs:
                    replica_dir = os.path.join(root, dirname)
                    source_dir = replica_dir.replace(replica_folder, source_folder, 1)

                    # Delete any directories in the replica directory that do not exist in the source directory
                    if not os.path.exists(source_dir):
                        shutil.rmtree(replica_dir)
                        log(log_file, f"deleted directory {replica_dir}")

            time.sleep(1)  # Sync every second

        # Catch any exceptions that may occur during the execution of the code in the try block
        except Exception as e:
            log(log_file, f"Error: {str(e)}")
            time.sleep(1)  # Retry after a second


def log(log_file, message):
    """
    This Function logs the message to a file with a timestamp.

    ->param log_file: path to the log file
    ->param message: message to log 
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_message = f"[{timestamp}] {message}"

    # Print the log message in terminal and log file
    print(log_message)
    with open(log_file, "a") as f:
        f.write(log_message + "\n")

if __name__ == "__main__":
    # Introduce the input for source folder, replica folder, and log file
    source_folder = input("Please introduce the path to the source folder: \n")
    replica_folder = input("Please introduce the path to the replica folder: \n")
    log_file = input("Please introduce the path to the log file: \n")

    sync_folders(source_folder, replica_folder, log_file)
