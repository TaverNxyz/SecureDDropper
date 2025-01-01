import pyautogui
import time
import keyboard
import os
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# Function to detect any of the images (runs on the same PC)
def find_images(image_names):
    for image_name in image_names:
        image_path = os.path.join("images", image_name)  # Path to images folder
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)  # Lowered confidence to 0.8
            if location is not None:
                return True
        except pyautogui.ImageNotFoundException:
            pass
    return False

# Function to click at a specific location (on the same PC)
def click_at(x, y):
    pyautogui.click(x, y)
    time.sleep(0.5)  # Adding a delay to simulate real-time interaction

# Function to simulate spacebar press (on the same PC)
def press_spacebar():
    keyboard.press('space')
    keyboard.release('space')
    time.sleep(0.1)

# Function to simulate 'y' key press (on the same PC)
def press_y():
    keyboard.press('y')
    keyboard.release('y')
    time.sleep(0.1)

# Main function to run the script
def run_script():
    print(Fore.YELLOW + "Please ensure that Escape From Tarkov is running.")
    print(Fore.YELLOW + "You have 5 seconds to prepare before the script starts.")
    time.sleep(5)  # 5-second delay to give the user time to switch to the game

    # Step 1: Mouse clicks for loading in (on the same PC)
    click_at(954, 643)  # 1st click
    click_at(958, 946)  # 2nd click
    click_at(890, 510)  # 3rd click
    click_at(1251, 1004)  # 4th click

    # Step 2: Fully pause and wait for any of 5.png, 8.png, 9.png, or 10.png to start spacebar spam (on the same PC)
    print(Fore.CYAN + "Waiting for any of 5.png, 8.png, 9.png, or 10.png to appear...")
    while not find_images(["5.png", "8.png", "9.png", "10.png"]):  # Pause until one of the images is found
        time.sleep(1)  # Check every second (you can adjust this timing if necessary)

    print(Fore.GREEN + "One of the images (5.png, 8.png, 9.png, or 10.png) found! Continuing with the script...")

    # After finding one of the images, repeatedly press spacebar until 6.png is found
    print(Fore.RED + "Pressing spacebar repeatedly until image 6.png is found...")
    while not find_images(["6.png"]):  # Check for 6.png while pressing spacebar
        press_spacebar()  # Keep pressing spacebar
        time.sleep(0.1)  # Adding a small delay between presses to avoid overloading the system

    print(Fore.GREEN + "Image 6.png found! Continuing the process.")

    # Additional actions like mouse clicks, key presses, etc.
    click_at(954, 1034)  # 5th click (coordinates after 6.png is found)
    print(Fore.CYAN + "5th mouse click executed.")

    # Now look for 7.png and press 'y' when found
    print(Fore.CYAN + "Waiting for image 7.png to appear...")
    while not find_images(["7.png"]):
        time.sleep(1)

    print(Fore.GREEN + "Image 7.png found! Pressing 'y' key.")
    press_y()

    # Search for 1.png, 11.png, 12.png, 13.png, or 14.png to restart the script
    print(Fore.RED + "Process complete. Waiting for 1.png, 11.png, 12.png, 13.png, or 14.png to restart the script.")
    while not find_images(["1.png", "11.png", "12.png", "13.png", "14.png"]):
        time.sleep(1)

    print(Fore.GREEN + "One of the restart images found! Restarting the script...")
    run_script()  # Re-run the script after finding one of the restart images

if __name__ == "__main__":
    run_script()
