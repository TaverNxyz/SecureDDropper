import pyautogui
import time
import os
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

def get_map_coordinates(map_choice):
    map_coords = {
        1: (770, 430),  # CUSTOMS
        2: (530, 560),  # SHORELINE
        3: (520, 560),  # STREETS
        4: (710, 390),  # FACTORY
        5: (880, 515),  # INTERCHANGE
        6: (440, 440)   # LIGHTHOUSE
    }
    return map_coords.get(map_choice)

def display_map_menu():
    print(Fore.CYAN + "\nSelect a map:")
    print(Fore.WHITE + "1. CUSTOMS")
    print(Fore.WHITE + "2. SHORELINE")
    print(Fore.WHITE + "3. STREETS")
    print(Fore.WHITE + "4. FACTORY")
    print(Fore.WHITE + "5. INTERCHANGE")
    print(Fore.WHITE + "6. LIGHTHOUSE")
    print(Fore.WHITE + "7. Exit")
    
    while True:
        try:
            choice = int(input(Fore.YELLOW + "\nEnter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print(Fore.RED + "Please enter a number between 1-7.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def get_run_count():
    while True:
        try:
            count = int(input(Fore.YELLOW + "\nHow many times would you like the script to run? (1-100): "))
            if 1 <= count <= 100:
                return count
            else:
                print(Fore.RED + "Please enter a number between 1 and 100.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def find_images(image_names):
    for image_name in image_names:
        image_path = os.path.join("images", image_name)
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location is not None:
                return True
        except Exception as e:
            print(Fore.GREEN + f"{Fore.RED} Loading Into Raid :) ...")
    return False

def click_at(x, y):
    try:
        pyautogui.click(x, y)
        time.sleep(0.5)
        print(Fore.GREEN + f"Clicked at coordinates ({x}, {y}).")
    except Exception as e:
        print(Fore.RED + f"Error clicking at coordinates ({x}, {y}): {e}")

def run_script(map_choice, current_run, total_runs):
    print(Fore.CYAN + f"\nStarting run {current_run} of {total_runs}")
    print(Fore.YELLOW + "Please ensure that Escape From Tarkov is running.")
    print(Fore.YELLOW + "You have 5 seconds to prepare before the script starts.")
    time.sleep(5)

    map_coords = get_map_coordinates(map_choice)
    if not map_coords:
        print(Fore.RED + "Invalid map selection!")
        return False

    # Initial clicks
    print(Fore.CYAN + "Performing initial clicks...")
    click_at(954, 643)  # 1st click
    click_at(958, 946)  # 2nd click

    print(Fore.CYAN + "Waiting for map selection screen...")
    time.sleep(2)

    # Click the map coordinates
    print(Fore.CYAN + f"Clicking selected map at coordinates {map_coords}...")
    click_at(*map_coords)
    print(Fore.GREEN + "Map selected!")
    time.sleep(0.5)

    click_at(1251, 1004)  # 4th click
    time.sleep(0.5)

    # Step 2: Wait for specific images to appear
    print(Fore.CYAN + "Waiting for specific images to appear...")
    while not find_images(["ICON IN RAID.png", "HUD ELEMENTS.png", "TOP LEFT PLAYER ICON.png"]):
        time.sleep(1)

    print(Fore.GREEN + "One of the images found! Continuing with the script...")

    # Spacebar spam until "RAID ENDED.png" is found
    print(Fore.RED + "Pressing spacebar repeatedly until 'RAID ENDED.png' is found...")
    while not find_images(["RAID ENDED.png"]):
        pyautogui.press('space')
        time.sleep(0.5)

    print(Fore.GREEN + "'RAID ENDED.png' found! Continuing the process.")

    # Final clicks and actions
    click_at(954, 1034)  # 5th click
    print(Fore.CYAN + "5th mouse click executed.")

    # Wait for "CLICK Y.png" and press 'y'
    print(Fore.CYAN + "Waiting for 'CLICK Y.png' to appear...")
    while not find_images(["CLICK Y.png"]):
        time.sleep(1)

    print(Fore.GREEN + "'CLICK Y.png' found! Pressing 'y' key.")
    pyautogui.press('y')

    # Restart process when specific images are found
    print(Fore.RED + "Process complete. Waiting to restart...")
    while not find_images(["ATTENTION.png", "CHARACTER.png", "TRADING.png", "HIDEOUT.png", "EFT.png"]):
        time.sleep(1)

    print(Fore.GREEN + "Restart images found! Restarting the script...")

if __name__ == "__main__":
    while True:
        map_choice = display_map_menu()
        if map_choice == 7:
            print(Fore.CYAN + "Exiting script. Goodbye!")
            break

        run_count = get_run_count()

        for current_run in range(1, run_count + 1):
            run_script(map_choice, current_run, run_count)
