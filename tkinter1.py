import tkinter as tk  # Import tkinter using lowercase alias 'tk'

window = tk.Tk()  # Create the main window object
window.title('Tkinter Sample Window')  # Set the title of the window
window.geometry('300x300')  # Set the dimensions of the window

# Label
greeting = tk.Label(window, text="Hello User", fg='black', bg='white')
# Button 
button = tk.Button(window, text="Click me", bg='black', fg='white')
# Entry 
entry = tk.Entry(window, fg="yellow", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

# Frame
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame.pack()
label = tk.Label(master=frame, text='Sample Frame')
label.pack()

# Textbox
textbox = tk.Text(window, fg='green', bg='yellow')
textbox.pack()

window.mainloop()  # Start the Tkinter event loop
