# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:12:42 2023

@author: Maruba
"""



class ArrayStack:
  """LIFO pile basée sur Python"""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # 

  def top(self):
    """Return (but do not remove) the element at the top of the stack.
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._data[-1]                 

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._data.pop()               # remove last item from list






if __name__ == '__main__':
    print("Salut Maruba")
    
    
    
    
    
    

