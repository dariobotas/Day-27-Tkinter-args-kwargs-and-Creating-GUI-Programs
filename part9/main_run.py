import tkinter as tk


def run():
  def button_clicked():
    hello.config(text=input.get())
    
  #Create GUI
  window = tk.Tk()
  window.title("Hello world")
  #Window minimum size
  window.minsize(500, 300)
  
  #create label
  hello = tk.Label(text="label", font=("Arial", 18, "bold"))
  hello.config(text="New Text")
  hello.grid(column=0, row=0)
  hello.config(padx=50, pady=50)
  #hello.pack()
  #hello["text"] = "New Text"
  
    
  #Button
  button = tk.Button(text="Click me!", command=button_clicked)
  button.grid(column=1,row=1)
  #button.pack()

    #Entry compponent
  input = tk.Entry(width=10)
  #input.pack()  
  print(input.get())
  input.grid(column=3,row=2)

  new_button = tk.Button(text="button")
  new_button.grid(column=2, row=0)

  #keeps on screen - needs to be the end of the program
  tk.mainloop()
