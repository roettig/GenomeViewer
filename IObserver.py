# -*- coding: utf-8 -*-
class IObserver(object):
   def __init__(self):
      if self.__class__ is IObserver:
         raise NotImplementedError
   def update(self,source,obj):
      raise NotImplementedError

