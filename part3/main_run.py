import tkinter as tk

def run():
  #Create GUI
  window = tk.Tk()
  window.title("Hello world")
  #Window minimum size
  window.minsize(500, 300)
  #window.geometry("300x300")

  #create label
  hello = tk.Label(text="Hello world!", font=("Arial", 18))
  #place it in the screen and center
  hello.pack(side="left")
  button = tk.Button(text="Click me!")
  button.pack()

  #keeps on screen - needs to be the end of the program
  tk.mainloop()

