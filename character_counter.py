import os
from collections import Counter

def get_file_paths(dir_path):
    file_paths = []
    total_files = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
            total_files += 1
    return file_paths, total_files
    
def get_file_names(file_paths):
    file_names = []
    for i in range(len(file_paths)):
        file_names.append(file_paths[i].split('\\')[-1])
        
    # next, remove the file extensions and "_"
    for i in range(len(file_names)):
        file_names[i] = file_names[i].split('.')[0]
        file_names[i] = file_names[i].replace('_', '')
        
    return file_names
       
def count_chars(file_names):
    # Here is where the magic happens and it counts every unique character and adds it to the counts dictionary
    counts = Counter()
    for name in file_names:
        counts.update(name)
    
    counts = sorted(counts.items(), key=lambda x: (x[0], x[1]))
    return counts

def main():
    source_folder = input("Enter the directory path: ")
    file_paths, total_files = get_file_paths(source_folder)
    file_names = get_file_names(file_paths)
    counts = count_chars(file_names)
    
    with open("character_counts.txt", 'w') as f:
        
        f.write("Source folder: " + source_folder + "\n\n")
        f.write("Total files: " + str(total_files) + "\n\n")
        f.write("Character counts:\n\n")
        
        for char, count in counts:
            f.write(f"\'{char}\': {count}\n")

    print(f"{total_files} files were processed from {source_folder}")
    print("The character counts are listed in character_counts.txt")

main()