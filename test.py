import tkinter as tk

# Event handler function for the label click
def label_clicked(event):
    print("Label clicked!")

# Create the main window
window = tk.Tk()
window.title("PythonExamples.org")
window.geometry("300x200")

# Take a background image
background_image = tk.PhotoImage(file="train.jpg")

# Create a label widget with background image
label = tk.Label(window, image=background_image, text="Hello World!", compound="center")

# Pack the label widget to display it
label.pack()

# Run the application
window.mainloop()