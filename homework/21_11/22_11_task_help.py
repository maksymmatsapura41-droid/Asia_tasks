"""
Подсказка к домашнему заданию
"""

from abc import ABCMeta, abstractmethod

# use ABCMeta as metaclass for Metric
class Metric():
    __slots__ = ("name",)

    def __init__(self, name: str):
        self.name = name

# this method should be abstract
    def collect(self) -> float:
        pass

# Metaclass for class factory creation
class MetricFactory(type):
    # here mcs - is a reference for metaclass. the same as cls for regular class and self for object
    def __new__(mcs, name, bases, namespace, **kwargs): # namespace is a dict with attributes
        value_name = namespace.get('__value_name__', 'value')
        cls =  None # call here super method for __new__
        cls.__slots__ = None # pass here tuple with value_name

        def __init__(self, value: float): # here u can initialize logic for every __init__ method of your constructor
            super(cls, self).__init__(name)
            # Add here validatation of attribute using self and _ validate method
            setattr(self, value_name, value) # setattr u can use to add some attributes to your object

        cls.__init__ = __init__ # in such way u set __init__ to every class created by this Metaclass

        def _validate(self, v):
            pass
            # add type and value validation according to the task

        cls._validate = _validate # in such way u can add method to every class created by this Metaclass

        def collect(self) -> float:
            pass
            # return value of metric using getattr method

        cls.collect = collect

        return cls # return class which was created

# Example of adding new metric. MemoryUsage, DiskUsage can be added exactly in the same way
class CpuUsage(Metric, metaclass=MetricFactory):
    __value_name__ = 'value'
