import os
import shutil

# Source and destination folders
source = "source_folder"
destination = "destination_folder"

# Make sure destination exists
if not os.path.exists(destination):
    os.makedirs(destination)

# Move all .jpg files
for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))
        print(f"Moved: {file}")

print("All .jpg files moved successfully!")
