import os
import shutil
import time
from math import ceil

# See folder_operations.py
             
def user_input():
    
    print("Welcome to the folder splitter. Please enter the following folder paths.")
    print("Tip: You can drag and drop the folder into the command prompt to get the path\n")
    temp_source = str(input("Enter source path: "))

    # Raw strings are produced from the inputted paths and then the subfolder name is extracted from the final block of text in the source path
    source_folder = repr(temp_source)[1:-1]
    path_array = temp_source.split('\\')
    sub_folder = path_array[-1] # Extract the subfolder name from the source path. No need for user input here

    temp_dest = str(input("Enter destination folder: "))
    destination_folder = repr(temp_dest)[1:-1]

    files_per_folder = int(input("How many files per folder? "))
    
    while True:
        operation = input("Do you want to 1: copy or 2: move the files? ")
        if operation == "1" or operation == "2":
            break
        else:
            print("Invalid operation. Please try again.")
    
    return source_folder, destination_folder, files_per_folder, sub_folder, operation

def file_operations(source_folder, destination_folder, files_per_folder, sub_folder, operation):
    
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Prepare the file operations
    files = os.listdir(source_folder)
    total_files = len(files)
    total_folders = ceil(total_files / files_per_folder)
    
    # File operations
    for i in range(total_folders):
        
        folder_path = make_sub_folder(destination_folder, sub_folder, i)
        
        # Determine the range of files for this folder
        start_index = i * files_per_folder
        end_index = min((i + 1) * files_per_folder, total_files)
        
        files.sort()
        counter = 1
        
        for file_name in files[start_index:end_index]:
            
            source_file = os.path.join(source_folder, file_name)
            
            # Get the file extension
            file_extension = os.path.splitext(file_name)[1]
            
            # Rename the file
            new_file_name = f"{counter}_{sub_folder}_{i+1}{file_extension}"
            destination_file = os.path.join(folder_path, new_file_name)
            
            if operation == "1":
                shutil.copy(source_file, destination_file)     
            elif operation == "2":
                shutil.move(source_file, destination_file)
                
            counter += 1
    
    if operation == "2":
        remove_folder(source_folder)   
        
    return total_files, total_folders

def make_sub_folder(destination_folder, sub_folder, i):
    
    folder_path = os.path.join(destination_folder, (sub_folder + "_" + str(i + 1)))
    os.makedirs(folder_path, exist_ok=True)
    print(f"New directory created: {folder_path}")  # Print statement for directory creation
    return folder_path
 
def remove_folder(source_folder):  
    try:
        os.rmdir(source_folder)
    except OSError:
        print(f"Error: {source_folder} could not be removed. It may not be empty.")
        
def main():
    source_folder, destination_folder, files_per_folder, sub_folder, operation = user_input()

    start_time = time.time() 
    total_files, total_folders = file_operations(source_folder, destination_folder, files_per_folder, sub_folder, operation)
    end_time = time.time() 
    time_taken = end_time - start_time
    minutes, seconds = divmod(time_taken, 60)

    if minutes > 0:
        print("All operations have been completed successfully!")
        print("Number of subfolders created: " + str(total_folders))
        print("Total files moved: " + str(total_files))
        print("Time taken: " + str(int(minutes)) + " minutes " + str(int(seconds)) + " seconds")
        input("Press enter to exit")
    else:
        print("All operations have been completed successfully!")
        print("Number of subfolders created: " + str(total_folders))
        print("Total files moved: " + str(total_files))
        print("Time taken: " + str(round(seconds, 2)) + " seconds")
        input("Press enter to exit")