from flask import Blueprint, jsonify, request
from src.main.factories.calculator_3_factory import calculator_3_factory
from src.main.factories.calculator_2_factory import calculator_2_factory
from src.main.factories.calculator_1_factory import calculator_1_factory

from src.errors.error_controlller import handle_errors

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
  try:
    calculator = calculator_1_factory()
    response = calculator.calculate(request)
    return jsonify(response), 200
  except Exception as e:
    error_response = handle_errors(e)
    return jsonify(error_response["body"]), error_response["status_code"]

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
  try:
    calculator = calculator_2_factory()
    response = calculator.calculate(request)
    return jsonify(response), 200
  except Exception as e:
    error_response = handle_errors(e)
    return jsonify(error_response["body"]), error_response["status_code"]

@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
  try:
    calculator = calculator_3_factory()
    response = calculator.calculate(request)
    return jsonify(response), 200
  except Exception as e:
    error_response = handle_errors(e)
    return jsonify(error_response["body"]), error_response["status_code"]