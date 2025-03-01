import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os

ascii_art = r"""
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||e |||m |||p |||e |||r |||i |||u |||m |||. |||t |||e |||c |||h ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

"""

class SplashScreen:
    def __init__(self, root, gif_path, exe_path, duration=1.5):
        self.root = root
        self.gif_path = gif_path
        self.exe_path = exe_path
        self.duration = int(duration * 1500)  # Convert to milliseconds for after()

        # Configure the window
        root.overrideredirect(True)  # Remove window border

        # Load the GIF to get its dimensions
        self.gif = Image.open(gif_path)
        width, height = self.gif.size

        # Set window size based on GIF dimensions
        root.geometry(f"{width}x{height}")

        # Center on screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")

        # Set up for animation
        self.frames = []
        self.current_frame = 0

        try:
            # Save all frames of the GIF
            while True:
                self.frames.append(ImageTk.PhotoImage(self.gif.copy()))
                self.gif.seek(self.gif.tell() + 1)
        except EOFError:
            pass  # End of frames

        # Create label to display the GIF
        self.label = tk.Label(root)
        self.label.pack()

        # Start animation
        self.animate()

        # Close splash & launch app after duration
        root.after(self.duration, self.close_splash)

    def animate(self):
        """ Updates the GIF animation frames """
        if self.frames:
            self.label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(50, self.animate)  # Update every 50ms

    def close_splash(self):
        """ Close the splash screen and wait for user input """
        print("Closing splash screen...")
        self.root.quit()  # Stop Tkinter mainloop but don't destroy the window immediately
        self.wait_for_user()  # Call the method to wait for user input

    def wait_for_user(self):
        """ Display ASCII art and wait for user input before launching main.exe """
        print(ascii_art)
        input("\nPress any key to continue...")

        print(f"Attempting to launch {self.exe_path}")
        try:
            subprocess.Popen(self.exe_path, shell=True, cwd=os.path.dirname(self.exe_path))
            print("Launching main.exe...")
        except Exception as e:
            print(f"Error launching executable: {e}")


if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build paths to the files
    gif_path = os.path.join(script_dir, "ezgif.com-optimize.gif")
    exe_path = os.path.join(script_dir, "jumppad.exe")

    # Create and run splash screen
    splash = tk.Tk()
    app = SplashScreen(splash, gif_path, exe_path, duration=1.5)
    splash.mainloop()
