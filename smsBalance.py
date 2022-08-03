import requests
import json

sms_balance_url = "https://api.umeskiasoftwares.com/api/v1/smsbalance"

check_balance_data = {
    "api_key": "SVQ4WVpPQUQ6NnpicDJsMm8=",
    "email": "alvo967@gmail.com"
}

check_balance_res = requests.post(sms_balance_url, data=json.dumps(check_balance_data))

# print(send_sms_res)
print(check_balance_res.json())