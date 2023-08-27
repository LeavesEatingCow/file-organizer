import tkinter as tk


class Organizer:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Organizer")

    # Run the app
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    organizer = Organizer()
    organizer.run()
