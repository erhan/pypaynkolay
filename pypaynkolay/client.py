import requests
import hashlib

class Client:
    def __init__(self, api_url, sx, secret_key):
        self.api_url =api_url
        self.sx = sx
        self.secret_key = secret_key

    def pos_init(self, amount, client_ref_code, success_url, fail_url, language="tr", use_3d=True, rnd=None, transaction_type="SALES", currency_code="TL", gsm=None):
        """
        Call Ortak Odeme Sayfasi endpoint.
        """
        url = f"{self.api_url}"
        data = {
            "sx": self.sx,
            "amount": amount,
            "clientRefCode": client_ref_code,
            "successUrl": success_url,
            "failUrl": fail_url,
            "language": language,
            "use3D": str(use_3d).lower(),
            "rnd": rnd,
            "transactionType": transaction_type,
            "currencyCode": currency_code,
            "gsm": gsm,
            # Hash data should be computed here
            "hashData": ""
        }

        response = requests.post(url, data=data)
        return response.content

    def complete_payment(self, sx, reference_code):
        """
        Call CompletePayment (3D işlemlerde) endpoint.
        """
        url = f"{self.api_url}/v1/CompletePayment"
        data = {
            "sx": sx,
            "referenceCode": reference_code
        }

        response = requests.post(url, data=data)
        return response.json()

    def cancel_payment(self, reference_code, trx_date, amount):
        """
        Call İptal Servisi endpoint.
        """
        url = f"{self.api_url}/v1/CancelRefundPayment"
        data = {
            "sx": self.sx,
            "referenceCode": reference_code,
            "trxDate": trx_date,
            "amount": amount,
            "type": "cancel",
            "resultUrl": "json",
            # Hash data should be computed here
            "hashData": self.compute_hash_data(reference_code, trx_date, amount)
        }

        response = requests.post(url, data=data)
        return response.json()

    def refund_payment(self, reference_code, trx_date, amount):
        """
        Call İade Servisi endpoint.
        """
        url = f"{self.api_url}/v1/CancelRefundPayment"
        data = {
            "sx": self.sx,
            "referenceCode": reference_code,
            "trxDate": trx_date,
            "amount": amount,
            "type": "refund",
            "resultUrl": "json",
            # Hash data should be computed here
            "hashData": self.compute_hash_data(reference_code, trx_date, amount)
        }

        response = requests.post(url, data=data)
        return response.json()

    def list_payments(self, start_date, end_date, client_ref_code):
        """
        Call Listeleme Servisi endpoint.
        """
        url = f"{self.api_url}/Payment/PaymentList"
        data = {
            "sx": self.sx,
            "startDate": start_date,
            "endDate": end_date,
            "clientRefCode": client_ref_code,
            # Hash data should be computed here
            "hashData": self.compute_hash_data(start_date, end_date, client_ref_code)
        }

        response = requests.post(url, data=data)
        return response.json()

    def compute_hash_data(self, *args):
        # Hash computation logic goes here.
        # You can use hashlib or hmac to compute the hash based on sx and secret_key.

        hash_string = "".join([str(arg) for arg in args]) + self.secret_key
        return hashlib.sha256(hash_string.encode()).hexdigest()