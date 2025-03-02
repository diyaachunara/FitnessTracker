import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class FitnessTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Fitness Tracker")
        self.root.state("zoomed")  # Make window full-screen

        # Load Background Image
        self.bg_image = Image.open("C:\\Users\\Dell\\OneDrive\\Desktop\\DSA project\\fitnessbg.jpg")  # Make sure this file exists!
        self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Set Background Label
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)  # Fill the entire window

        self.create_widgets()

    def create_widgets(self):
        button_font = ('Helvetica', 14, 'bold')
        label_font = ('Helvetica', 14)

        # Frame to Hold Widgets
        frame = tk.Frame(self.root, bg="white", bd=5)
        frame.place(relx=0.5, rely=0.5, anchor="center")  # Center widgets

        # Steps Entry
        tk.Label(frame, text="Enter Steps:", font=label_font, bg="white").pack(pady=10)
        self.steps_entry = tk.Entry(frame, font=('Helvetica', 12))
        self.steps_entry.pack(pady=5)

        # Calculate Button
        self.calculate_button = tk.Button(frame, text="Calculate Distance & Calories", command=self.calculate, font=button_font, bg="#4CAF50", fg="white", relief="raised", bd=2)
        self.calculate_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(frame, text="Exit", command=self.root.quit, font=button_font, bg="#F44336", fg="white", relief="raised", bd=2)
        self.exit_button.pack(pady=10)

    def calculate(self):
        try:
            steps = int(self.steps_entry.get())
            distance_km = steps * 0.0008  
            calories_burned = steps * 0.04  
            messagebox.showinfo("Results", f"Distance: {distance_km:.2f} km\nCalories Burned: {calories_burned:.2f} calories")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numerical value for steps.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
