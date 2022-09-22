from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def 0(self)
  self.tr()
  self.put5()
  self.tl()
  self.m()
  self.put2()
  self.tl()
  self.put5()
  self.tl()
  self.m()
  self.put2()
  self.ta()
  self.m()
  self.m()
  self.m()
  self.m()
  self.tr()
  self.m()
  self.m()
  self.m()
  self.m()
  
  def mm(self,num):
  for number in range(num):
    self.m()
  def m0(self,num):
  for number in range(num):
    self.0()

    
    def main():
    """ Karel code goes here! """
    kt = ktools()
      self.m()
      self.tl()
      self.put5()
      self.tr()
      self.m()
      self.tr()
      self.mm(5)
      self.m0(15)
     

   
    pass


if __name__ == "__main__":
    run_karel_program()