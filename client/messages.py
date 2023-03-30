from phone import Phone

phone_number = "555-555-523"
secret_key = "793a3f1d3fafdea1f28de6cc27c0a6b6"
phone = Phone(phone_number, secret_key)

# Get all messages for phone number
response = phone.make_request("https://Day-1.railenbailen.repl.co/get_messages", {"number": phone_number, "secret_key": secret_key})
print(response)