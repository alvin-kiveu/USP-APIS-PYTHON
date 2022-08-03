import requests
import json

send_sms_url = "https://api.umeskiasoftwares.com/api/v1/sms"

send_sms_data = {
    "api_key": "SVQ4WVpPQUQ6NnpicDJsMm8=",
    "email": "alvo967@gmail.com",
    "Sender_Id": "23107",
    "message": "Iko poa sasa",
    "phone":"254768168060"
}

send_sms_res = requests.post(send_sms_url, data=json.dumps(send_sms_data))

print(send_sms_res.json())
