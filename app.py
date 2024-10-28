# This is the main code for my daily tracker app. The goal is that the user will be able to:
#   1. record and track meals (times and portion sizes)
#   2. record and track exercise (times of the day, number of reps)
#   3. record weight (amount, as well as image)
#   4. record daily activities (acts as a diary at first)
#   5. record spending and savings (not with actual money, however. Merely a tracker for the money, not a store)

#----------------------------------------------------------------------------------------------------------------------------------------
# Making the data store:
#   -Started here
#   - Will hold all the imports
#   - This portion will handle how the data the user inputs will be stored.
#   - Written input (e.g. weight in number, entry of meals e.t.c) will be stored in a text file.
#   - visual input (e.g. pictures of meals, pictures taken in weigh-ins) will be stored as JPGs in separate folders.

#imports
import os
import tkinter as tk

#code for defining the directories for storage
DATA_DIR=r"D:\tracker data\test data"
IMG_DIR=r"D:\tracker data\Images"
MEALS_FILE=os.path.join(DATA_DIR, "MEALS.txt")
WEIGHT_FILE=os.path.join(DATA_DIR, "WEIGHT.txt")
SPENDING_FILE=os.path.join(DATA_DIR, "SPENDING.txt")
DAILIES_FILE=os.path.join(DATA_DIR, "DAILY_ACTIVITIES.txt")
MEAL_IMG_DIR=os.path.join(IMG_DIR, "MEAL_IMG")
WEIGHT_IMG_DIR=os.path.join(IMG_DIR, "WEIGHINS")

#code for creating the directory files of they don't exist on your computer
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(MEAL_IMG_DIR, exist_ok=True)
os.makedirs(WEIGHT_IMG_DIR, exist_ok=True)
#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------
#Creating the handlers:
#   -Will be used when the buttons on the homepage are clicked.
#   -Handles everything that will happen in the home page in general

def meal_tracking():
    print(".")
def exercise_tracking():
    print(".")
def weight_tracking():
    print(".")
def dailies_tracking():
    print(".")
def show_rules():
    print(".")
#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------
#Creating the home page:
#   - This will be the main link to other operations in the app
#   - Will have buttons for the meals, weighing, spending and daily activities page.
#   - Will also have buttons for displaying the rules at the bottom corner of the screen. Opposite to it will be the exit button

#code for creating the page
root = tk.Tk()
root.title("Daily tracker")
root.geometry("400x500")

#code for creating the buttons
meals_button = tk.Button(root, text="Meals", command=meal_tracking, width="20", height="2").pack(pady=20)
exercise_button = tk.Button(root, text="Exercise", command=exercise_tracking, width="20", height="2").pack(pady=20)
weight_button = tk.Button(root, text="weight", command=weight_tracking, width="20", height="2").pack(pady=20)
dailies_button = tk.Button(root, text="Day's notes", command=dailies_tracking, width="20", height="2").pack(pady=20)

#code for the rules and exit button
bottom_frame = tk.Frame(root).pack(side="bottom", fill="x", pady=10)
rules_button = tk.Button(bottom_frame, text="Rules", command=show_rules, width=10, height=1, bg="blue").pack(side="left", padx=10)
exit_button = tk.Button(bottom_frame, text="Exit", command=exit, width=10, height=1, bg="red").pack(side="right", padx=10)

root.mainloop()

