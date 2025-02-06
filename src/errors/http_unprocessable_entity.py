class HttpUnProcessableEntityError(Exception):
  def __init__(self, message: str) -> None:
    self.message = message
    self.name= "UnprocessableEntity"
    self.status_code=422
