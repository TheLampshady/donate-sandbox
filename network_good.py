import json
import requests
from urllib2 import Request, urlopen


class NetworkGood(object):

    def __init__(self, host):
        self.host = host
        self.auth_token = ""

    def auth(self):
        headers = {'Content-Type': 'application/json'}

        payload = {
          "source": "NFGAPIARYTEST",
          "userid": "NFGAPIARYTESTUSER",
          "password": "F5t2GYu#",
          "scope": "donation donation-reporting"
        }

        url = self.host + '/access/rest/token'

        # Requests lib
        # r = requests.post(url, json=payload, headers=headers)
        # resp_json = json.loads(r.content)

        request = Request(url, data=json.dumps(payload), headers=headers)
        response_body = urlopen(request).read()
        resp_json = json.loads(response_body)
        self.auth_token = resp_json['token']

    def donate(self, ein):
        url = self.host + '/service/rest/donation'
        url = self.host + '/service/rest/donation/paypal'

        donation = {
                "organizationId": ein,
                "organizationIdType": "Ein",
                "designation": "Emergency Shelter",
                "dedication": "In honor of someone",
                "amount": "1.00",
                "feeAddOrDeduct": "Deduct",
                "transactionType": "Donation",
              }


        # totalAmount (number) - Amount of all line items in donation
        # "totalAmount": 60.41,
        # "tipAmount": 0,
        # OriginalDonationPartnerTransactionID (string, optional) - Partner transaction id of original donation
        # "partnerTransactionId": "a2ebf708-4056-41bb-8a09-23a88d441ac0",
        payment = {
            "donor": {
                "ip": "50.121.129.54",
                "token": "802f365c-ed3d-4c80-8700-374aee6ac62c"
            },
            "payPal": {
                  "returnUrl": "https://megadonors.org/paypal-return.jsp",
                  "cancelUrl": "https://megadonors.org/paypal-cancel.jsp"
            }
        }

        payload = {
            "source": "NFGAPIARYTEST",
            "campaign": "API",
            "donationLineItems": [donation],
            "payment": payment
         }

        headers = {
          'Authorization': 'Bearer %s' % self.auth_token,
          'Content-Type': 'application/json'
        }

        request = Request(url, data=json.dumps(payload), headers=headers)

        response_body = urlopen(request).read()
        print response_body