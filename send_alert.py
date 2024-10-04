import requests
from requests.auth import HTTPBasicAuth

# Exotel credentials (replace with your actual SID, token, and other details)
EXOTEL_SID = 'wfs661'  # Replace with your Exotel SID
EXOTEL_TOKEN = 'b5b1da3695743779baba0b63b020f8872c8932012d258ca3'  # Replace with your Exotel Token
EXOTEL_VIRTUAL_NUMBER = '09513886363'  # Your Exotel virtual number (landline)

def send_sms(to_number, message):
    url = f"https://api.exotel.com/v1/Accounts/{EXOTEL_SID}/Sms/send.json"
    
    # Request payload
    payload = {
        'From': EXOTEL_VIRTUAL_NUMBER,  # Use Exotel's provided virtual number
        'To': to_number,
        'Body': message
    }

    # Making the request with basic authentication
    try:
        response = requests.post(url, data=payload, auth=HTTPBasicAuth(EXOTEL_SID, EXOTEL_TOKEN))
        
        if response.status_code == 200:
            print("SMS sent successfully")
        else:
            print(f"Failed to send SMS: {response.status_code}, {response.text}")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    to_number = "+918886991813"  # Replace with actual recipient phone number
    message = "Weather Alert: Severe weather conditions expected. Stay safe."
    send_sms(to_number, message)
