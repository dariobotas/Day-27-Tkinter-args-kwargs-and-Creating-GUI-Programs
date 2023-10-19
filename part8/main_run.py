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
  input.insert(0, string="Some text to begin with.")
  print(input.get())
  input.pack()  
  print(input.get())

  #Text
  text = tk.Text(height=5, width=30)
  #Puts cursor in textbox.
  text.focus()
  #Adds some text to begin with.
  text.insert(END, string="Example of multi-line text entry.")
  #Get's current value in textbox at line 1, character 0
  print(text.get("1.0", 0))
  text.pack()

#Spinbox
  def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
  spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
  spinbox.pack()

#Scale
#Called with current scale value.
  def scale_used(value):
      print(value)
  scale = tk.Scale(from_=0, to=100, command=scale_used)
  scale.pack()

  #Checkbutton
  def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
  checked_state = IntVar()
  checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
  checked_state.get()
  checkbutton.pack()

  #Radiobutton  
  def radio_used():
    print(radio_state.get())
  #Variable to hold on to which radio button value is checked.
  radio_state = IntVar()
  radiobutton1 = tk.Radiobutton(text="Option1",     value=1, variable=radio_state, command=radio_used)
  radiobutton2 = tk.Radiobutton(text="Option2", value=2,    variable=radio_state, command=radio_used)
  radiobutton1.pack()
  radiobutton2.pack()


  #Listbox
  def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

  listbox = tk.Listbox(height=4)
  fruits = ["Apple", "Pear", "Orange", "Banana"]
  for item in fruits:
    listbox.insert(fruits.index(item), item)
  listbox.bind("<<ListboxSelect>>", listbox_used)
  listbox.pack()

  
  #keeps on screen - needs to be the end of the program
  tk.mainloop()
