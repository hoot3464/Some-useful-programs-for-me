import os
import time
import signal
import subprocess

# This program is a launcher for my most used programs using folders from my Desktop
# It is meant to be used with a keyboard shortcut
# It also plays some awesome music in the background
# It also works as a game launcher!

def folder_menu():
    
    print("Welcome to my awesome program launcher! Please select a folder below.\n")
    
    desktop_path = os.path.expanduser("~/Desktop")
    dir_names = [name for name in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, name))]

    # Folder menu
    while True:
        for i, name in enumerate(dir_names, start=1):
            print(f"{i}. {name}")

        print("\n0. Exit\n")
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
           exit()
        
        if 0 <= choice <= len(dir_names):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            

    # Program name and path are stored for the program menu
    os.system('cls')
    program_name = dir_names[choice-1]
    dir_path = os.path.join(desktop_path, dir_names[choice-1])
    return dir_path, program_name

def program_menu(link_names, program_name):
    
    print(f"\nWelcome to {program_name}! Please select a program below.\n")
    
    # Program menu with back button functionality
    while True:
        for i, name in enumerate(link_names, start=1):
            name_without_ext = os.path.splitext(name)[0]
            print(f"{i}. {name_without_ext}")

        print("\n0. Go Back")
        print("00: Exit\n")
        
        choice = input("Enter your choice: ")
        
        # Exit option is different from folder menu
        if choice == "00":
            exit()
        else:
            choice = int(choice)
        if 0 <= choice <= len(link_names):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    
    return choice

def main():
    
    music_path = r"E:\Music\Main Menu Favorites_mp3"
    vlc = subprocess.Popen([r"C:\Program Files\VideoLAN\VLC\vlc.exe", "--playlist-tree", music_path, "--random", "--qt-start-minimized"])
    exit_flag = False
    
    # Initiates the folder menu and back button functionality
    while True:
        dir_path, program_name = folder_menu()
 
        # Prepares the program menu
        link_dict = {i+1: file for i, file in enumerate(os.listdir(dir_path))}
        link_names = list(link_dict.values())

        choice = program_menu(link_names, program_name)
        if choice == 0:
            continue
        else:
            break

    print(f"Preparing to launch {link_names[choice-1]}")
    time.sleep(2)
    print(f"Launching {link_dict[choice]}")    
    music_kill = input("Do you want the music to keep playing? (y/n) ")
    if music_kill == "n":
        os.kill(vlc.pid, signal.SIGTERM)
        
    os.startfile(os.path.join(dir_path, link_dict[choice]))
    time.sleep(2)

main()