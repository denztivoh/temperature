#class to do.....
class Temperature:
  def __init__(self, celsius):
    self.celsius= celsius
  def to_fahrenheit(self):
    return (self.celsius*1.5) + 30
  def to_celsius(self, fahrenheit):
    return (fahrenheit - 30)/1.5
temp = Temperature(30)
print("Temperature in fahrenheit:", temp.to_fahrenheit())
print("Temperature in celsius:", temp.to_celsius(40))