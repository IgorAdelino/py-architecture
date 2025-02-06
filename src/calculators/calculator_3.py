from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import Request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnProcessableEntityError
from src.errors.http_bad_request import HttpBadRequestError


class Calculator3:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest)-> Dict:
    body = request.json

    input_data = self.__validate_body(body)

    variance = self.__calculate_variance(input_data)

    multiplication = self.__calculate_multiplication(input_data)

    self.__verify_results(variance, multiplication)

    formated_response = self.__format_response(variance)

    return formated_response


  def __validate_body(self, body: Dict) -> float:
      if "numbers" not in body or not isinstance(body["numbers"], list):
          raise HttpUnProcessableEntityError("Invalid body")

      if not all(isinstance(n, (int, float)) for n in body["numbers"]):
          raise HttpUnProcessableEntityError("Invalid body")
    
      input_data = body["numbers"]
      return input_data
  
  def __calculate_variance(self, numbers: List[float]) -> float:
     variance = self.__driver_handler.variance(numbers)
     return variance
  
  def __calculate_multiplication(self, numbers: List[float]) -> float:
     multiplication = 1
     for num in numbers: multiplication *= num
     
     return multiplication
  
  def __verify_results(self, variance: float, multiplication: float) -> None:
     if variance < multiplication:
        raise HttpBadRequestError("Process Failed: Variance is less than multiplication")
     
  def __format_response(self, variance: float) -> Dict:
    return {
      "data": {
        "Calculator": 3,
        "Result": variance,
        "Success": True
      }
    }