import sys
import os
from PIL import Image

# Grab first and second argument from command line input
imageFolder = sys.argv[1]
outputFolder = sys.argv[2]

print(imageFolder, outputFolder)
# Check if /new exists, if not create
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Loop through imageFolder
# Convert images to PNG
# Save to the new folder
for eachFileName in os.listdir(imageFolder):
    img = Image.open(f"{imageFolder}\\{eachFileName}")
    # Removed the .jpg extension text at the end of the files
    clean_name = os.path.splitext(eachFileName)[0]

    img.save(f"{outputFolder}\\{clean_name}.png", "png")
    print("Success, all done!")
