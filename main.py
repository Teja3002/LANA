import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import subprocess

# Create the main window
window = tk.Tk()

# Set the background color to yellow
window.configure(bg="#FFE607")

# Set the window size and position
window.geometry("800x600")

# Define a custom font
custom_font = font.Font(family="Fedroka_One", size=20, weight="bold")

# Function to run when the image is clicked
def start_program1():
    program_path = "C:/Users/Teja Krishna/PycharmProjects/LANA Desktop/distance.py" # Replace with the actual path to your program
    global process1
    process1 = subprocess.Popen(["python", program_path])  # Launch the program using Python

def start_program2():
    program_path = "C:/Users/Teja Krishna/PycharmProjects/LANA Desktop/neck.py" # Replace with the actual path to your program
    global process2
    process2 = subprocess.Popen(["python", program_path])  # Launch the program using Python

# Add some widgets to the window
label1 = tk.Label(window, text="LANA", fg="black", bg="#FFE607", font=custom_font)
label1.pack(pady=(50, 100))
label1.place(relx=0.52, rely=0.1, anchor=tk.N)

rectangle = tk.Canvas(window, width=3000, height=500, bg="#645A5A")
rectangle.place(relx=0.1, rely=0.8, anchor=tk.CENTER)

# Load and display the image with transparency
image_path = "C:/Users/Teja Krishna/Downloads/distance.jpg"
image = Image.open(image_path)
image = image.resize((150, 150))
photo = ImageTk.PhotoImage(image)

# Create a label with the image and bind the click event to the function
image_label = tk.Label(window, image=photo, bg="#645A5A")
image_label.image = photo
image_label.pack()
image_label.place(relx=0.2, rely=0.8, anchor=tk.S)

label2 = tk.Label(window, text="Distance Monitoring", fg="black", bg="#645A5A", font=custom_font)
label2.pack(pady=(50, 100))
label2.place(relx=0.2, rely=0.45, anchor=tk.N)

# Load and display the second image with transparency
image_path = "C:/Users/Teja Krishna/Downloads/neck.png"
image = Image.open(image_path)
image = image.resize((150, 150))
photo = ImageTk.PhotoImage(image)

# Create a label with the second image and bind the click event to the function
image_label = tk.Label(window, image=photo, bg="#645A5A")
image_label.image = photo
image_label.pack()
image_label.place(relx=0.8, rely=0.8, anchor=tk.S)

label3 = tk.Label(window, text="Posture Monitoring", fg="black", bg="#645A5A", font=custom_font)
label3.pack(pady=(50, 100))
label3.place(relx=0.8, rely=0.45, anchor=tk.N)

# Function to handle the first switch state change
def toggle_switch1():
    switch_state.set(not switch_state.get())
    if switch_state.get():
        switch_button.config(text="ON", relief=tk.SUNKEN, bg="green")
        start_program1()
    else:
        switch_button.config(text="OFF", relief=tk.RAISED, bg="red")
        if process1:
            process1.terminate()

# Create the first switch button
switch_button = tk.Button(window, text="OFF", relief=tk.RAISED, bg="red", command=toggle_switch1)
switch_button.pack(pady=20)
switch_button.place(relx=0.2, rely=0.9)

# Function to handle the second switch state change
def toggle_switch2():
    switch_state.set(not switch_state.get())
    if switch_state.get():
        switch_button2.config(text="ON", relief=tk.SUNKEN, bg="green")
        start_program2()
    else:
        switch_button2.config(text="OFF", relief=tk.RAISED, bg="red")
        if process2:
            process2.terminate()

# Create the second switch button
switch_button2 = tk.Button(window, text="OFF", relief=tk.RAISED, bg="red", command=toggle_switch2)
switch_button2.pack(pady=20)
switch_button2.place(relx=0.8, rely=0.9)

switch_state = tk.BooleanVar()
switch_state.set(False)

# Start the main loop
window.mainloop()
