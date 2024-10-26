# This is the main code for my daily tracker app. The goal is that the user will be able to:
#   1. record and track meals (times and portion sizes)
#   2. record and track exercise (times of the day, number of reps)
#   3. record weight (amount, as well as image)
#   4. record daily activities (acts as a diary at first)
#   5. record spending and savings (not with actual money, however. Merely a tracker for the money, not a store)

# Making the data store:
#   -Started here
#   - This portion will handle how the data the user inputs will be stored.
#   - Written input (e.g. weight in number, entry of meals e.t.c) will be stored in a text file.
#   - visual input (e.g. pictures of meals, pictures taken in weigh-ins) will be stored as JPGs in separate folders.

#imports
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Image, ImageTk
#from PIL import Image, ImageTk

#defining directories
DATA_DIR = r"D:\tracker data\text data"
IMAGE_DIR = r"D:\tracker data\Images"
MEALS_FILE = os.path.join(DATA_DIR, 'meals.txt')
WEIGHT_FILE = os.path.join(DATA_DIR, 'weight.txt')
SPENDING_FILE = os.path.join(DATA_DIR, 'spending.txt')
DAILIES_FILE = os.path.join(DATA_DIR, 'daily_activites.txt')
MEAL_IMAGES_DIR = os.path.join(IMAGE_DIR, 'meals')
WEIGHIN_IMAGES_DIR = os.path.join(IMAGE_DIR, 'weigh-ins')

#creating the directories (if they don't exist on your computer)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(MEAL_IMAGES_DIR, exist_ok=True)
os.makedirs(WEIGHIN_IMAGES_DIR, exist_ok=True)

#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------TO BE CONTINUED---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------

#Creating the meals page:
#   -Made this after the button handlers
#   - This will be used in the page for meal tracking
#   - User data for that day will be populated on the screen
#   - should there be no data added that day, there will be a box that, when clicked, allows the use to add data. This box will alway be
#      present under the boxes for the meals eaten that day
#   - There will also be buttons for declaring fasting days and seeing records of previous days, as well as returning to the home page.

# creating fasting day list
fasting_days = []
# code for loading the day's meals on the page
def today_meals():
    today = datetime.now().date().isoformat()
    meals = []
    if os.path.exists(MEALS_FILE):
        with open(MEALS_FILE, 'r') as file:
            for line in file:
                date, time, meal_type, contents, notes, image_path = line.strip().split(', ')
                if date == today:
                    meals.append({
                        "date": date,
                        "time": time,
                        "type": meal_type,
                        "contents": contents,
                        "notes": notes,
                        "image_path": image_path
                    })
    return meals

# code for saving meal data to the text file
def save_meal(meal):
    with open(MEALS_FILE, 'a') as file:
        file.write(f"{meal['date']}, {meal['time']}, {meal['type']}, {meal['contents']}, {meal['notes']}, {meal['image_path']}\n")

# code for the new meal window
def add_meal():
    if datetime.now().weekday() in fasting_days:
        messagebox.showinfo("Fasting day", "Today is a fasting day. Stick to it! You can't input meals today.")
        return
    add_window = tk.Toplevel()
    add_window.title("Add meal")
    tk.Label(add_window, text="Meal type (e.g., Breakfast, Lunch, Dinner, Snack): ").pack()
    meal_type_entry = tk.Entry(add_window)
    meal_type_entry.pack()
    tk.Label(add_window, text="Contents: ").pack()
    contents_entry = tk.Entry(add_window)
    contents_entry.pack()
    tk.Label(add_window, text="Notes: ").pack()
    notes_entry = tk.Entry(add_window)
    notes_entry.pack()
    
    def get_image():
        img_path = filedialog.askopenfilename(filetypes=[("JPG files", "*.jpg")])
        if img_path:
            img_entry.delete(0, tk.END)
            img_entry.insert(0, img_path)
    
    tk.Button(add_window, text="Choose image", command=get_image).pack()
    img_entry = tk.Entry(add_window)
    img_entry.pack()
    
    def save_new_meal():
        meal_type = meal_type_entry.get()
        contents = contents_entry.get()
        notes = notes_entry.get()
        img_path = img_entry.get()
        today = datetime.now().date().isoformat()
        current_time = datetime.now().time().strftime("%H:%M")
        
        meal = {
            "date": today,
            "time": current_time,
            "type": meal_type,
            "contents": contents,
            "notes": notes,
            "image_path": img_path
        }
        save_meal(meal)
        messagebox.showinfo("Success", "Meal saved successfully.")
        add_window.destroy()
        update_meal_list()
    
    tk.Button(add_window, text="Save meal", command=save_new_meal).pack()

# code that updates the meal page every time a meal is added
def update_meal_list():
    for widget in meal_frame.winfo_children():
        widget.destroy()
    meals = today_meals()
    for meal in meals:
        frame = tk.Frame(meal_frame)
        frame.pack(fill="x", pady=5)
        if os.path.exists(meal['image_path']):
            img = Image.open(meal['image_path'])
            img.thumbnail((50, 50))
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.pack(side="left", padx=5)
        else:
            img_label = tk.Label(frame, text="No image", width=10, height=5, bg="grey")
            img_label.pack(side="left", padx=5)
        meal_info = f"{meal['type']} at {meal['time']} - {meal['contents']} - {meal['notes']}"
        meal_label = tk.Label(frame, text=meal_info, anchor="w", justify="left")
        meal_label.pack(side="left", padx=5)
    tk.Button(meal_frame, text="Add meal", command=add_meal, bg="lightgrey").pack(pady=10)

#Creating the button handlers:
#   - Made this after the buttons for the home page
#   - will be used after the buttons on the home page are clicked
#   - redirects to different pages which is where the user will add all their details

def meal_tracking():
    meal_window = tk.Toplevel(root)
    meal_window.title("Today's meals")
    meal_window.geometry("400x500")
    global meal_frame
    meal_frame = tk.Frame(meal_window)
    meal_frame.pack(fill="both", expand=True)
    
    def view_records():
        date = simpledialog.askstring("View records", "Enter a date (YYYY-MM-DD): ")
        if date:
            pass  # Placeholder. Will finish later
    
    def add_fasting_day():
        day = simpledialog.askinteger("Fasting day", "Enter day number: 0-Monday, 1-Tuesday, ..., 6-Sunday")
        if day is not None and 0 <= day <= 6:
            fasting_days.append(day)
            messagebox.showinfo("Success", f"Day {day} set as fasting day.")
        else:
            messagebox.showerror("Invalid input", "Enter a number between 0 and 6")
    
    tk.Button(meal_window, text="View past records", command=view_records).pack(pady=5)
    tk.Button(meal_window, text="Declare fasting day", command=add_fasting_day).pack(pady=5)
    tk.Button(meal_window, text="Home", command=meal_window.destroy, bg="blue").pack(pady=5)
    update_meal_list()

def exercise_tracking():
    print(".")  # TO BE CONTINUED

def weighin_tracking():
    print(".")  # TO BE CONTINUED

def dailies_tracking():
    print(".")  # TO BE CONTINUED

def exit_app():
    root.quit()

#Creating the home page:
#   - This portion will handle the page that shows when the application is first started
#   - will have buttons for all the available options(meal tracking, weight tracking, spending tracking, daily activities), as well as 
#       an exit button.

root = tk.Tk()
root.title("Daily tracker")
root.geometry("400x400")

#Creating the buttons
meal_button = tk.Button(root, text="Meals", command=meal_tracking, width="20", height="2")
meal_button.pack(pady=20)
exercise_button = tk.Button(root, text="Work-outs", command=exercise_tracking, width="20", height="2")
exercise_button.pack(pady=20)
weight_button = tk.Button(root, text="Weight", command=weighin_tracking, width="20", height="2")
weight_button.pack(pady=20)
dailies_button = tk.Button(root, text="Day's activities", command=dailies_tracking, width="20", height="2")
dailies_button.pack(pady=20)
exit_button = tk.Button(root, text="Exit", command=exit_app, width="20", height="2", bg="red")
exit_button.pack(pady=20)

root.mainloop()
