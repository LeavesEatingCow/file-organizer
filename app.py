import tkinter as tk
import os
import shutil


class Organizer:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Organizer")
        self.window.geometry("800x800")

    # Run the app
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    organizer = Organizer()
    organizer.run()
