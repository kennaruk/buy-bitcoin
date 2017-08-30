import hashlib
import hmac
import time
import json
import base64

API_KEY = 'vh6OTEhEl6AjKAfn8QJ8exhOstIvI8WPRdw75YD4'  # Replace this with your API Key
API_SECRET = 'e2B2ZGjapi6WwH4jDYvRku8jQvNLBvpP9L6OQT9uvVwnPIurvs'  # Replace this with your API secret


def get_nonce():
    """Return a nonce based on the current time.

    A nonce should only use once and should always be increasing.
    Using the current time is perfect for this.
    """
    # Get the current unix epoch time, and convert it to milliseconds
    return int(time.time() * 1e6)


def sign_request(url, nonce, body=None):
    """Return an HMAC signature based on the request."""
    if body is None:
        # GET requests don't have a body, so we'll skip that for signing
        message = str(nonce) + url
    else:
        body = json.dumps(body, separators=(',', ':'))
        message = str(nonce) + url + body

    return str(
        hmac.new(
            bytes('vh6OTEhEl6AjKAfn8QJ8exhOstIvI8WPRdw75YD4'.encode('utf-8')),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
    )
