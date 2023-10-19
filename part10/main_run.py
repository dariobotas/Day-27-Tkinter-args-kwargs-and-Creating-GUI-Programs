import tkinter as tk
  

def run():    
  
  def calculate_miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609344, 2)
    km_value_label.config(text=f"{km}")
  
  #Create GUI
  window = tk.Tk()
  window.title("Mile to Km Converter")
  window.config(padx=28, pady=28)

  miles_entry = tk.Entry()
  miles_entry.grid(column=1,row=0)

  miles_label = tk.Label(text="Miles")
  miles_label.grid(column=2, row=0)

  equal_label = tk.Label(text="is equal to")
  equal_label.grid(column=0, row=1)
  
  km_value_label = tk.Label(text=0)
  km_value_label.grid(column=1, row=1)

  km_label = tk.Label(text="Km")
  km_label.grid(column=2, row=1)

  calculate_button = tk.Button(text="Calculate",command=calculate_miles_to_km)
  calculate_button.grid(column=1, row=2)
  
  #keeps on screen - needs to be the end of the program
  tk.mainloop()
