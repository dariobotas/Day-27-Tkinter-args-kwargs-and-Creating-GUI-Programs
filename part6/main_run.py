import tkinter as tk
import part6.playground as pl

def run():
  #Create GUI
  window = tk.Tk()
  window.title("Hello world")
  #Window minimum size
  window.minsize(500, 300)
  num = pl.calculate(2, add=3, multiply=5)
  #create label
  hello = tk.Label(text=f"label: {num}", font=("Arial", 18))
  #place it in the screen and left
  hello.pack(side="left")
  button = tk.Button(text="Click me!")
  button.pack()

  #keeps on screen - needs to be the end of the program
  tk.mainloop()

""" Unlimited Arguments
    def add(n1, n2):
      return n1 + n2

    add(n1=5, n2=3)

    def add(*args):
      for n in args:
        print(n)

    add(1,2,3,4,5,6,7,8,9,0)
      """