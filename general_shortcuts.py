import os
import time
import signal
import subprocess


def main():
    
    music_path = r"E:\Music\Main Menu Favorites_mp3"
    vlc = subprocess.Popen([r"C:\Program Files\VideoLAN\VLC\vlc.exe", "--playlist-tree", music_path, "--random", "--qt-start-minimized"])
    
    while True:
        dir_path = input("Enter the directory path: ")
        if os.path.isdir(dir_path):
            break
        else:
            print("Invalid directory path. Please enter a valid path.")

    link_dict = {i+1: file for i, file in enumerate(os.listdir(dir_path))}
    link_names = list(link_dict.values())

    while True:
        for i, name in enumerate(link_names, start=1):
            name_without_ext = os.path.splitext(name)[0]
            print(f"{i}. {name_without_ext}")

        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(link_names):
            break
        else:
            print("Invalid choice. Please enter a valid number.")

    print(f"Preparing to launch {link_names[choice-1]}")
    time.sleep(2)
    print(f"Launching {link_dict[choice]}")
    os.startfile(os.path.join(dir_path, link_dict[choice]))
    os.kill(vlc.pid, signal.SIGTERM)

main()