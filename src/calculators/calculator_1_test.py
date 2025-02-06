from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises

class MockRequest:
  def __init__(self, body: Dict)-> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest({"number": 1})

  calculator1 =  Calculator1()

  response = calculator1.calculate(mock_request)
  
  # Response format
  assert "data" in response
  assert "Calculator" in response['data']
  assert "result" in response["data"]

  # Response value
  assert response["data"]["result"] == 14.24740748999224
  assert response["data"]["Calculator"] == 1

def test_calculate_with_body_eror():
  mock_request = MockRequest({"number": "a"})

  calculator1 =  Calculator1()
  with raises(Exception) as excinfo:
    calculator1.calculate(mock_request)
  assert str(excinfo.value) == "Invalid body"
  
