import tkinter as tk
from tkinter import messagebox

# Fitness Tracker Application
class FitnessTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Fitness Tracker")
        self.root.geometry("400x300")  # Adjusted smaller window size

        self.create_widgets()

    def create_widgets(self):
        button_font = ('Helvetica', 14, 'bold')  # Adjusted font size for buttons
        label_font = ('Helvetica', 14)

        # Steps Entry
        tk.Label(self.root, text="Enter Steps:", font=label_font).pack(pady=10)
        self.steps_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.steps_entry.pack(pady=5)

        # Calculate Button
        self.calculate_button = tk.Button(self.root, text="Calculate Distance & Calories", command=self.calculate, font=button_font, bg="#4CAF50", fg="white", relief="raised", bd=2)
        self.calculate_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=button_font, bg="#F44336", fg="white", relief="raised", bd=2)
        self.exit_button.pack(pady=10)

    def calculate(self):
        try:
            # Get the input value for steps
            steps = int(self.steps_entry.get())

            # Estimating the distance (0.0008 km per step)
            distance_km = steps * 0.0008  # 0.8 meters per step = 0.0008 km per step

            # Estimating the calories burned (0.04 calories per step)
            calories_burned = steps * 0.04  # 0.04 calories per step

            # Show the results
            messagebox.showinfo("Results", f"Distance: {distance_km:.2f} km\nCalories Burned: {calories_burned:.2f} calories")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numerical value for steps.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
