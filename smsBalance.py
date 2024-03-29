import requests

def get_sms_balance(api_key, email):
    url = "https://api.umeskiasoftwares.com/api/v1/smsbalance"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": api_key,
        "email": email
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage:
api_key = "VE5MTlkzRk06MTlwNjlkZWM="
email = "example@gmail.com"

response = get_sms_balance(api_key, email)
print(response)
