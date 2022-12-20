import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Add a label to the window
label = tk.Label(window, text="Press the button:")
label.pack()

# Add a button to the window
count = 0
def button_clicked():
  global count
  count += 1
  if count >= 20:
    button.config(state="disabled", bg="#e74c3c")
    label.config(text="Sluta trycka")
  else:
    label.config(text=str(count))
button = tk.Button(window, text="Click me!", command=button_clicked)
button.pack()

# Set the font and size of the label
label.config(font=("Verdana", 16))

# Set the background color and size of the button
button.config(bg="#2ecc71", fg="#ffffff", font=("Verdana", 24), width=10, height=2, relief="groove", bd=0)

# Run the Tkinter event loop
window.mainloop()
