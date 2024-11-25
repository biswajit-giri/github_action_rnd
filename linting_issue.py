import os,sys

def calc_sum(a,b ):
  sum=a+b
  if(sum> 10 ):
      print('Sum is greater than 10')
  else:
      print('Sum is',sum)
  return sum

class MyClass:
  def __init__(self,name):
      self.name = name
      self.age = 25
      self.height = 180

  def display(self):
      print 'Name: ' + self.name  # Python 2 style print
      print "Age: ",self.age  # Inconsistent string quotes
      print ('Height:',self.height )  # Misplaced space

  def get_height(self):
      return self.height
