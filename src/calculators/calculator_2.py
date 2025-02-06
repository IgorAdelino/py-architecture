from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.numpy_hanlder import NumpyHandler

class Calculator2:
  def calculate(self, request: FlaskRequest)-> Dict:
    body = request.json

    input_data = self.__validate_body(body)
    calculated_number = self.__process_data(input_data)
    print("calculated_number", calculated_number)
    formated_response = self.__format_response(calculated_number)

    return formated_response


  def __validate_body(self, body: Dict) -> List[float]:
      if "numbers" not in body or not isinstance(body["numbers"], list):
          raise Exception("Invalid body")

      if not all(isinstance(n, (int, float)) for n in body["numbers"]):
          raise Exception("Invalid body")
    
      input_data = body["numbers"]
      return input_data
  
  def __process_data(self, input_data: List[float]) -> float:
     numpy_handler = NumpyHandler()
     first_process_result = [(num * 11) ** 0.95 for num in input_data]
     result = numpy_handler.standard_derivation(first_process_result)
     return 1 / result
  
  def __format_response(self, calculated_number: float) -> Dict:
    return {
      "data": {
        "Calculator": 2,
        "result": calculated_number
      }
    }


     