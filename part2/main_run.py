import tkinter as tk

def run():
  window = tk.Tk()
  window.title("Hello world")
  window.geometry("300x300")

  hello = tk.Label(text="Hello world!")
  hello.pack()
  button = tk.Button(text="Click me!")
  button.pack()

  tk.mainloop()

