# build_script.py
import PyInstaller.__main__
import os

# Create the images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

PyInstaller.__main__.run([
    'your_script.py',  # Replace with your script's filename
    '--onefile',  # Create a single executable
    '--add-data', 'images/*.png;images',  # Include all PNG files from images folder
    '--hidden-import', 'PIL._tkinter_finder',  # Required for PyAutoGUI
    '--name', 'EFTAutomation',  # Name of the output executable
    '--icon', 'NONE',  # No icon (remove this line if you want to add an icon)
])