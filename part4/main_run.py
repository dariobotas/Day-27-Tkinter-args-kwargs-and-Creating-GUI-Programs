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
  #place it in the screen and left
  hello.pack(side="left")
  button = tk.Button(text="Click me!")
  button.pack()

  #keeps on screen - needs to be the end of the program
  tk.mainloop()


  """ Keyword Arguments 
      def my_function(a, b, c):
      Do this with a
      Then do this with b
      Finnaly do this with c
      my_function(1,2,3)
      
      Arguments with Default Values
      def my_function(a=1, b=2, c=3):
      Do this with a
      Then do this with b
      Finnaly do this with c
      my_function(b=5) or my_function(a=3) the other values are defaulted
      
      """