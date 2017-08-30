import requests
import hmac_example

url = 'https://coins.ph/api/v3/crypto-accounts/'
nonce = hmac_example.get_nonce()
signature = hmac_example.sign_request(url, nonce)

headers = {
    'ACCESS_SIGNATURE': signature,
    'ACCESS_KEY': hmac_example.API_KEY,
    'ACCESS_NONCE': nonce,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
print ('header')
print (headers)
req = requests.get(url, headers=headers)
print (req)


# EXPECTED RESPONSE
# {
#    "crypto-accounts":[
#       {
#          "id":"2r45ab4",
#          "name":"Default Account",
#          "currency":"BTC",
#          "balance":"1.5",
#          "pending_balance":"0.00000000",
#          "default_address":"1a2a3c4b"
#       }
#    ]
# }
