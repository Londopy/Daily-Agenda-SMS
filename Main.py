import os
import feather
import vonage
import pandas as pd
import schedule
import time

from nexmo import Client

# Replace YOUR_API_KEY and YOUR_API_SECRET with your actual API key and secret
client = vonage.Client(key="YOUR_API_KEY", secret="YOUR_API_SECRET")
sms = vonage.Sms(client)

def send_message():
		"""Sends a message with a daily schedule."""
		# Read the schedule from the feather file
		df = pd.read_feather('schedule.feather')
		schedule_text = df.to_string(index=False)

		# Set the recipient and message body
		recipient_phone_number = "NUMBER"
		message = schedule_text

		# Send the SMS message
		response = sms.send_message(
			{
				"from":"YOUR_VONAGE_PHONE_NUMBER",
				"to": recipient_phone_number,
				"text": message
			}
		)
		if response["messages"][0]["status"] == "0":
			print("Message sent successfully.")
			print(response)
		else:
			print(f"Message failed with error: {response['messages'][0]['error-text']}")
		

## Display the GUI to edit the schedule
#df = pd.read_feather('schedule.feather')
#feather.show(df)
#df.to_feather('schedule.feather')

# Set the schedule to run every day at 5:59 AM
schedule.every().day.at("05:59").do(send_message)

# Run the send_message function once when the program starts
send_message()

while True:
	schedule.run_pending()
	time.sleep(60)  # Wait one minute before checking the schedule again
