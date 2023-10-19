import tkinter as tk


def run():
  #Create GUI
  window = tk.Tk()
  window.title("Hello world")
  #Window minimum size
  window.minsize(500, 300)
  
  #create label
  hello = tk.Label(text="label", font=("Arial", 18))
  hello.pack()

  hello["text"] = "New Text"
  hello.config(text="New Text")
 
  #challenge 1
  def button_clicked():
    #hello.config(text="Got clicked")
    #challenge 2
    hello.config(text=input.get())
    
  #Button
  button = tk.Button(text="Click me!", command=button_clicked)
  button.pack()

    #Entry compponent
  input = tk.Entry(width=10)
  input.pack()  
  print(input.get())

  #keeps on screen - needs to be the end of the program
  tk.mainloop()
