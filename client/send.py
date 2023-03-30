from phone import Phone

phone_number = "555-555-523"
secret_key = "793a3f1d3fafdea1f28de6cc27c0a6b6"
phone = Phone(phone_number, secret_key)

recipient_number = "555-555-5555"
message = "Hello, this is a test message."
phone.send_message(recipient_number, message)