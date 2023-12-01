import os
import shutil
import time

# See folder_operations.py

def merge_folders(source_folders, destination_folder):
    
    os.makedirs(destination_folder, exist_ok=True)

    for source_folder in source_folders:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                shutil.move(os.path.join(root, file), destination_folder)
    
    for source_folder in source_folders:
        shutil.rmtree(source_folder)

def main():
    
    source_folders = input("Enter source folder paths, separated by commas: ").split(',')
    destination_folder = input("Enter destination folder path: ")
    
    start_time = time.time()
    merge_folders(source_folders, destination_folder)
    end_time = time.time() 
    time_taken = end_time - start_time 
    
    print("All the files have been moved successfully to " + destination_folder)
    print(f"Time taken: {time_taken:.2f} seconds")
    input("Press enter to exit")
    
main()