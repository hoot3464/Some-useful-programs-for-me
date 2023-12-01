import os
from collections import Counter

# This program counts the number of times each character appears in the file names of a directory
# It was created show the importance of the Counter class in the collections module
# With just a few lines of code, it can count every unique character in a list of strings
# There are only a few characters that can be used for file names, but this program would work if there were more
# This program was also made to help me find special characters in files that I may have missed when renaming them
# The special characters may mess with other file operations in other programs

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
        
    # For the purposes of this program, the underscores and file extensions are removed
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

def write_to_file(source_folder, total_files, counts):
    with open("character_counts.txt", 'w') as f:
        
        f.write("Source folder: " + source_folder + "\n")
        f.write("Total files: " + str(total_files) + "\n")
        f.write("Character counts:\n\n")
        
        for char, count in counts:
            f.write(f"\'{char}\': {count}\n")

def main():
    source_folder = input("Enter the directory path: ")
    file_paths, total_files = get_file_paths(source_folder)
    file_names = get_file_names(file_paths)
    counts = count_chars(file_names)
    
    write_to_file(source_folder, total_files, counts)

    print(f"{total_files} files were processed from {source_folder}")
    print("The character counts are listed in character_counts.txt")

main()