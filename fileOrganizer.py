import os
import shutil

# Define dictionary mapping file extensions to destination folders
file_types = {
    # Images
    "--images--------": (
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".psd", ".svg", ".webp"
    ),

    # Documents
    "--documents-----": (
        ".pdf", ".docx", ".doc", ".odt", ".ods", ". odp",
        ".rtf", ".csv", ".html", ".css", ".json", ".xml"
    ),

    # Videos
    "--videos--------": (".mp4", ".avi", ".mkv", ".wmv", ".mov", ".flv", ".webm"),

    # Audio
    "--audio---------": (".mp3", ".wav", ".flac", ".ogg", ".aac", ".m4a", ".wma"),

    # Archives
    "--archives------": (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"),

    # 3D models
    "--3d models-----": (".stl", ".fbx", ".obj", ".gltf", ".glb", ".blend", ".unitypackage"),

    # Code
    "--code----------": (
        ".py", ".java", ".cpp", ".js", ".cs", ".php", ".html", ".css", ".json"
    ),

    # Presentations
    "--presentations--": (".pptx", ".ppt", ".ppsx", ".pps", ". odp"),

    # Spreadsheets
    "--spreadsheets---": (".xlsx", ".xls", ".ods", ".drawio"),

    # Text files
    "--text files-----": (".txt", ".rtf", ".md"),

    # Fonts
    "--fonts---------": (".ttf", ".otf", ".woff", ".woff2"),

    # Executables
    "--executables----": (".exe", ".bat", ".sh"),

    # System files
    "--system files---": (".dll", ".sys", ".cpl"),

    # Data files
    "--data files-----": (".db", ".dat"),

    # Others
    "--others--------": None,
}

# Define the base download directory (modify as needed)
download_dir = "C:/Users/user/Downloads/"  # Replace with your actual path


destination_folder_name = "FOLDERS"


def organize_downloads():
    for filename in os.listdir(download_dir):
        # Get the file extension (lowercase)
        extension = os.path.splitext(filename)[1].lower()

        print(f"Detected extension for '{filename}': {extension}")  # Print detected extension
        
        if os.path.isdir(os.path.join(download_dir, filename)):
            # Skip folders (avoid moving them)
            print(f"Skipping folder '{filename}'.")
            continue  # Skip remaining processing for folders
        
        # Find the destination folder based on the extension
        destination_folder = None
        for folder_name, extensions in file_types.items():
            if extensions is not None and extension in extensions:  # Check for None
                destination_folder = folder_name
                break
            else:
                destination_folder = "--others--------"
        

        # Create the destination folder if it doesn't exist
        if destination_folder and not os.path.exists(os.path.join(download_dir, destination_folder)):
            os.makedirs(os.path.join(download_dir, destination_folder))

        # Move the file to the destination folder
        if destination_folder:
          source = os.path.join(download_dir, filename)
          dest = os.path.join(download_dir, destination_folder, filename)
          shutil.move(source, dest)
          print(f"Moved '{filename}' to '{destination_folder}' folder.")
        else:  # If destination_folder is None (meaning a file belongs to "others")
          source = os.path.join(download_dir, filename)
          dest = os.path.join(download_dir, destination_folder, filename)
          shutil.move(source, dest)
          print(f"File '{filename}' has no specific category, moved to 'others' folder.")

# Call the organization function

skip_categories = set(file_types.keys())  # Extract category names as a set

def move_folders():
    # Create the destination folder if it doesn't exist
    if not os.path.exists(os.path.join(download_dir, destination_folder_name)):
        os.makedirs(os.path.join(download_dir, destination_folder_name))

    # Move folders to the destination folder
    for item in os.listdir(download_dir):
        # Check if it's a folder (not a file), skip "FOLDERS", and avoid categories
        if (
            os.path.isdir(os.path.join(download_dir, item))
            and item != destination_folder_name
            and item.lower() not in skip_categories
        ):
            source = os.path.join(download_dir, item)
            dest = os.path.join(download_dir, destination_folder_name, item)
            shutil.move(source, dest)
            print(f"Moved folder '{item}' to '{destination_folder_name}'.")

# Call the folder moving function
organize_downloads()
move_folders()