from twilio.rest import Client
import twilio_details

client_instance = Client(twilio_details.acc_sid, twilio_details.auth_token)

message = client_instance.messages.create(to=twilio_details.to, from_=twilio_details.sender,
                                          body="Test Text Message from Twilio")

print("Message sent successfully.")
