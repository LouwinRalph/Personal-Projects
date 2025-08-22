import tkinter as tk

window = tk.Tk()
window.title("Meow")
#window.geometry("800x600")

screen = tk.Canvas(window, width=800, height=600)
screen.pack()
#screen.configure(bg="red")
def on_button_click():
        textbox.insert("1")

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()
 
textbox = tk.Text(window, height=10, width=40) 
textbox.pack()

window.mainloop()