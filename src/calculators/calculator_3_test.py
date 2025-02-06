from .calculator_3 import Calculator3
from typing import Dict, List
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

mock_driver = NumpyHandler()

class MockDriverHandler(DriverHandlerInterface):
  def standard_derivation(self, numbers: List[float]) -> float:
    return 3
  
  def variance(self, numbers: List[float]) -> float:
    return 2

def test_calculate_with_integration():
  calculator_3 = Calculator3(driver_handler=mock_driver)

  mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
  response = calculator_3.calculate(mock_request)

  assert response["data"]["Success"] == True

def test_calculate_with_variance_error():
  mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

  calculator_3 = Calculator3(driver_handler = mock_driver)

  with raises(Exception) as excinfo:
    calculator_3.calculate(mock_request)


  assert str(excinfo.value) == "Process Failed: Variance is less than multiplication"