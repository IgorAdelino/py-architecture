class HttpBadRequestError(Exception):
  def __init__(self, message: str) -> None:
    self.message = message
    self.name= "BadRequestError"
    self.status_code=400
