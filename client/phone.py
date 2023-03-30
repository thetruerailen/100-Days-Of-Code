import requests


class Phone:
    def __init__(self, number, secret_key):
        self.number = number
        self.secret_key = secret_key
    
    # Helper method to make API requests
    def make_request(self, endpoint, data):
        headers = {"Content-Type": "application/json"}
        result = requests.post(endpoint, headers=headers, json=data)
        return result.json()

    def send_message(self, to, message):
      endpoint = "https://Day-1.railenbailen.repl.co/send_message"
      data = {
          "number": self.number,
          "secret_key": self.secret_key,
          "to": to,
          "message": message
      }
      result = self.make_request(endpoint, data)
      if "message" in result:
          print(result["message"])
      elif "error" in result:
          print(result["error"])
      else:
          print("Unknown error occurred.")