from stanfordkarel import *


class ktools:
  def m(self):
     move()

  def tl(self):
      turn_left


  def tr(self):
        self.tl()
        self.tl()
        self.tl()

  def pick(self):
      pick_beeper

  def put(self):
       put_beeper
  def ta(self):
    turn_left()
    turn_left()

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
     self.put5()
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

   
 




def main():
   """ Karel code goes here! """
   kt=ktools()
   kt.h()
   pass


if __name__ == "__main__":
    run_karel_program()