class InvalidInputError(Exception):
      pass

#NameError is build in exceptions

      
def process_input(value):
    if value < 0:
        raise InvalidInputError("Input must be non-negative")
    return value ** 0.5
    
try:
    print(process_input(-5))
    
except InvalidInputError as e:
    print(f"Error: {e}")