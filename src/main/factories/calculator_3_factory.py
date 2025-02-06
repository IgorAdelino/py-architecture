from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

def calculator_3_factory():
  numpy_handler = NumpyHandler()
  calc = Calculator3(driver_handler=numpy_handler)
  return calc