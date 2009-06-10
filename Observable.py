# -*- coding: utf-8 -*-
class Observable(object):
   """
   Observable is an abstract base class for concrete Observable
   classes that want to make use of the Observer pattern to
   notify registered objects of any changes.
   """

   _observers = []
   _changed   = False

   def __init__(self):
      """
      Default constructor.
      Enforces abstractness by prohibition of instantiation
      """
      if self.__class__ is Observable:
         raise NotImplementedError


   def addObserver(self,observer):
      """
      Adds an object to the list of observers.
      """
      self._observers.append( observer )


   def removeObserver(self,observer):
      """
      Removes an object from the list of observers
      """
      if(self._observers.count(observer)>0):
         self._observers.remove(observer)

   def notifyObservers(self,obj):
      """
      Notify all registered observers of change
      """
      for observer in self._observers:
          observer.update(self,obj)


   def hasChanged(self):
      """
      Returns whether the data has changed
      """
      return self._changed

   def clearChanged(self):
      """
      Set status to unchanged
      """
      self._changed = False

   def setChanged(self):
      """
      Set status to changed
      """
      self._changed = True
      self.notifyObservers(self)



