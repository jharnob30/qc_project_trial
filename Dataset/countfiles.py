import os

# Specify the directory path
directory = 'E:\Projects\BDMLI PROJECTS\Dataset\Category3-Styling'

# Initialize a dictionary to store folder names and their respective file counts
folder_file_counts = {}

# Iterate over each item in the directory
for item in os.listdir(directory):
    # Construct the full path of the item
    item_path = os.path.join(directory, item)
    
    # Check if the item is a directory
    if os.path.isdir(item_path):
        # Count the number of files in the directory
        file_count = len([name for name in os.listdir(item_path) if os.path.isfile(os.path.join(item_path, name))])
        
        # Store the folder name and its file count in the dictionary
        folder_file_counts[item] = file_count

# Print the folder names and their respective file counts
for folder, count in folder_file_counts.items():
    print(f"{folder} {count}")
