from stanfordkarel import *


class ktools:
 def m(self):
   """M shorthand for move"""
 move()

def tl(self):
  turn_left


  def tr(self):
    """turn around"""
  self.tl()
  self.tl()
  self.tl()


  Def.ta(self)
  """turn around"""
  self.tl()
  Self.tl()
  
  def pick(self):
   pick_beeper

  def put(self):
   put_beeper


def put2(self):
 self.put()
 self.m()
 self.put()


def put5(self):
 self.put2()
 self.m()
 self.put2()
 self.m()
 self.put()

def h(self):
 self.tl()
 self.tr()
 self.m()
 self.m()
 self.m()
 self.tr()
 self.put5()
 self.ta()
 self.m()
 self.m()
 self.tl()
 self.m()
 self.put2()
 self.tl()
 self.m()
 self.m()
 self.tl()
 self.m()
 self.m()
 self.m()
 self.m()

def fic(self):
  """front is clear"""
  return front_is_clear

def fib(self):
  """front is blocked"""
  return not self.fic()
def ric(self):
    self.tr()
    if self.fic():
     self.tl()
     return True
    self.tl()
    return False
  



def mm(self,num):
  for number in range(num):
    self.m()


def pickm(self,num):
   for i in range(num-1):
     self.pick()
     self.m()
     self.pick()
def putm(self,num):
  self.put()
  self.m()

  
def rib(self):
  """right is blocked"""
  return not self.ric()

def mazemove(self):
  if self.fib():
    self.tl()
  else:
    self.m()
    if self.ric():
      self.tr()
      self.m()
      if self.ric():
        self.tr()
        self.m()



  pass
      
  

def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.tl()
    kt.mm(5)
    kt.ta()
    kt.putm(5)
    kt.tl()
    kt.mm(2)
    pass


if __name__ == "__main__":
    run_karel_program()