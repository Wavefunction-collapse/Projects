# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:31:52 2020

@author: Nikolai
"""



def mult():
     sumn = 0
     for x in  range(1000):
        if  (x % 3 == 0 or x % 5 == 0):
            sumn = sumn + x
            print(sumn)    
            


     
  
    

if __name__ == "__main__":   
   print(mult())  
   
   #for n in  range(1000):
      # print(mult(n))
    