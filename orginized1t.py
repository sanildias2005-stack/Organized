import os
import shutil

def organize_junk(directory):
    # Define the mapping of extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Video': ['.mp4', '.mkv', '.mov'],
        'Archives': ['.zip', '.tar', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.html', '.css']
    }

    # Change to the target directory
    os.chdir(directory)

    for file in os.listdir():
        # Skip directories, we only want files
        if os.path.isfile(file):
            filename, extension = os.path.splitext(file)
            extension = extension.lower()

            # Find which category the file belongs to
            moved = False
            for folder, extensions in file_types.items():
                if extension in extensions:
                    # Create folder if it doesn't exist
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    
                    # Move the file
                    shutil.move(file, os.path.join(folder, file))
                    print(f"Moved: {file} -> {folder}/")
                    moved = True
                    break
            
            # Optional: Move unknown types to an "Others" folder
            if not moved:
                if not os.path.exists('Others'):
                    os.makedirs('Others')
                shutil.move(file, os.path.join('Others', file))

if __name__ == "__main__":
    target_path = input("Enter the full path of the folder to organize: ").strip().replace('"', '')
    
    if os.path.isdir(target_path):
        organize_junk(target_path)
        print("Done! Your files are now organized.")
    elif os.path.isfile(target_path):
        print("❌ Error: You provided a path to a FILE. Please provide a path to a FOLDER.")
    else:
        print("❌ Error: That path doesn't seem to exist. Check for typos!")