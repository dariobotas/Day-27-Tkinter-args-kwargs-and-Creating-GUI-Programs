def add(*args):
  #print(args[0])
  sum = 0
  for n in args:
    sum += n
  return sum

def calculate(n, **kwargs):
  print()
  for key, value in kwargs.items():
    print(key)
    print(value)

  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

  print(kwargs["add"])
  return n

calculate(2, add=3, multiply=5)

class Car:

  def __init__(self, **kw):
    self.make = kw.get("make")
    self.model = kw.get("model")
    self.color = kw.get("color")
    self.seates = kw.get("seats")

  #in this way the arguments are mandatory and we need to fill every time we create an Object
  #def __init__(self, **kw):
  #  self.make = kw["make"]
  #  self.model = kw["model"]

my_car = Car(make="Nissa")
print(my_car.model())