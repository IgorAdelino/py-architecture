from typing import Dict, List
from .calculator_2 import Calculator2
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


def test_calculate():
  mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
  calculator_2 = Calculator2(driver_handler=MockDriverHandler())
  response =calculator_2.calculate(mock_request)

  # Response format
  assert isinstance(response, dict)

  # Response value
  assert response["data"]["result"] == 0.3333333333333333
  assert response["data"]["Calculator"] == 2


def test_calculate_integration():
  mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
  calculator_2 = Calculator2(driver_handler=mock_driver)
  response =calculator_2.calculate(mock_request)

  # Response format
  assert isinstance(response, dict)

  # Response value
  assert response["data"]["result"] == 0.08095934764697119
  assert response["data"]["Calculator"] == 2

def test_calculate_with_body_eror():
  mock_request = MockRequest({"number": "a"})

  calculator1 =  Calculator2(driver_handler = mock_driver)
  with raises(Exception) as excinfo:
    calculator1.calculate(mock_request)
  assert str(excinfo.value) == "Invalid body"
