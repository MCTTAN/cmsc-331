import abc

class Bird(abc.ABC):
  @abc.abstractmethod
  def fly(self):
    pass

class Parrot(Bird):
  pass
  def fly(self):
    print("Flying Parrot")

p = Parrot()
p.fly()

-----

class Bird(abc.ABC):
  @abc.abstractmethod
  def fly(self):
    pass

class Robot(Bird):
  pass
  def fly(self):
    print("Flying Robot")
    
class RoboDragon(Bird, Robot):
  pass
  def fly(self):
    print("RoboDragon")
    
