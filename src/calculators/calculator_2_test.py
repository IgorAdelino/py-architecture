from typing import Dict
from .calculator_2 import Calculator2
from pytest import raises

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
  calculator_2 = Calculator2()
  response =calculator_2.calculate(mock_request)

  # Response format
  assert isinstance(response, dict)

  # Response value
  assert response["data"]["result"] == 0.08095934764697119
  assert response["data"]["Calculator"] == 2

def test_calculate_with_body_eror():
  mock_request = MockRequest({"number": "a"})

  calculator1 =  Calculator2()
  with raises(Exception) as excinfo:
    calculator1.calculate(mock_request)
  assert str(excinfo.value) == "Invalid body"
