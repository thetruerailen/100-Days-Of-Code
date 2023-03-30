from flask import Flask, request, jsonify
import os
import json


app = Flask(__name__)
data_dir = os.path.join(os.getcwd(), "json_data")
numbers_file = os.path.join(data_dir, "numbers.json")
keys_file = os.path.join(data_dir, "keys.json")
messages_file = os.path.join(data_dir, "messages.json")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)


# Helper function to read data from the JSON files
def read_json_file(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


# Helper function to write data to the JSON files
def write_json_file(data, file):
    with open(file, "w") as f:
        json.dump(data, f)


# Endpoint to register a phone number and generate a secret key
@app.route("/register_number", methods=["POST"])
def register_number():
    number = request.json["number"]
    numbers = read_json_file(numbers_file)
    if number in numbers:
        return jsonify({"message": f"Number {number} already registered."})
    secret_key = os.urandom(16).hex()
    numbers[number] = secret_key
    write_json_file(numbers, numbers_file)
    return jsonify({"secret_key": secret_key})


# Endpoint to send a message
@app.route("/send_message", methods=["POST"])
def send_message():
    number = request.json["number"]
    secret_key = request.json["secret_key"]
    message = request.json["message"]
    numbers = read_json_file(numbers_file)
    messages = read_json_file(messages_file)
    if number not in numbers or numbers[number] != secret_key:
        return jsonify({"message": "Invalid number or secret key."})
    messages[number].append(message)
    write_json_file(messages, messages_file)
    return jsonify({"message": "Message sent."})


# Endpoint to get all messages for a phone number
@app.route("/get_messages", methods=["POST"])
def get_messages():
    number = request.json["number"]
    secret_key = request.json["secret_key"]
    numbers = read_json_file(numbers_file)
    messages = read_json_file(messages_file)
    if number not in numbers or numbers[number] != secret_key:
        return jsonify({"message": "Invalid number or secret key."})
    return jsonify({"messages": messages[number]})




if __name__ == "__main__":
    if not os.path.exists(numbers_file):
        write_json_file({}, numbers_file)
    if not os.path.exists(keys_file):
        write_json_file({}, keys_file)
    if not os.path.exists(messages_file):
        write_json_file({}, messages_file)
    app.run(debug=True, host="0.0.0.0", port=8080)