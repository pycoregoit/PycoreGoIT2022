# classes
# OOP

# rex = Dog()
# rex - instance; object; екземпляр


class Dog:
  """Model of dog"""

  def __init__(self, name, age):
    """Initialize attributes name and age"""
    self.name = name
    self.age = age

  def sit(self):
    """Dog sit"""
    print(self.name.title() + " is sitting now")

  def roll_over(self):
    """Dog is roll over"""
    print(self.name.title() + " rolled over")

rex = Dog("rex", 3)
# print(rex)  # object
print("My dog name is " +  rex.name)
print("My dog age is " +  str(rex.age))

rex.sit()
rex.roll_over()

bob = Dog("bob", 10)
print("Your dog name is " +  bob.name)
print("Your dog age is " +  str(bob.age))

bob.sit()
bob.roll_over()


lala = Dog("lala")


class Car:
  """Model of car"""

  def __init__(self, make, model, year):
    """Inicialize car atributes"""
    self.make = make
    self.model = model
    self.year = year
    self.odometr = 0

  def correct_name(self):
    """Correct name of car"""
    long_name = str(self.year) + " " + self.make + " " + self.model
    return long_name.title()

  def read_odometer(self):
    """How many kilometers car ride in km"""
    print("This car has " + str(self.odometr) + " km")

  def update_odometer(self, kilometers):
    """Update odometer value"""
    if kilometers >= self.odometr:
      self.odometr = kilometers
    else:
      print("You can't roll back an odometer")

  def increase_odometer(self, kilometers):
    """Increase kilometers value"""
    self.odometr += kilometers


new_car = Car("mercedes", "s600", 2020)
print(new_car.correct_name())
new_car.read_odometer()

new_car.odometr = 50
new_car.read_odometer()


bmw = Car("bmw", "x5", "2018")
print(bmw.correct_name())
bmw.update_odometer(40000)
bmw.read_odometer()

bmw.increase_odometer(1000)
bmw.read_odometer()


class Battery:
  def __init__(self, battery=40):
    self.battery = battery

  def battery_inf(self):
    """Show battery information"""
    print("This car has a " + str(self.battery) + "kWh")

  def get_range(self):
    if self.battery == 40:
      range = 150
    elif self.battery == 75:
      range = 280

    message = "This car can approximately go " + str(range)
    print(message)

class ElectricCar(Car):
  """Model for electric cars"""

  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery()

  def battery_inf(self):
    """Show battery information"""
    print("This car has a " + str(self.battery) + "kWh")


nissan_leaf = ElectricCar("nissan", "leaf", 2017)
print(nissan_leaf.correct_name())
nissan_leaf.battery_inf()
nissan_leaf.battery.get_range()


class Dog:
    vyd = "animal"

    def __init__(self, name, age):
        """Initialize attributes name and age"""
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def sit(self):
        """Dog sit"""
        print(self.name.title() + " is sitting now")

    def roll_over(self):
        """Dog is roll over"""
        print(self.name.title() + " rolled over")


class FrenchBuldog(Dog):
    pass


class Vivcharka(Dog):
    pass


rex = Vivcharka("rex", 5)
lala = FrenchBuldog("lala", 3)

rex.sit()

lala.roll_over()

print("Type ", type(rex))

print(isinstance(rex, Vivcharka))

print(isinstance(rex, Dog))