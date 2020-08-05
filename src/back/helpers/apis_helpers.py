import json
import decimal
import traceback
import sys
from flask import jsonify


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class CustomError:
    local = True

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def throw(self):
        if self.local:
            etype, value, tb = sys.exc_info()
            tracelist = ['Traceback (most recent call last):\n']
            tracelist = traceback.format_tb(tb, 2000)
        else:
            tracelist = []

        return jsonify({
            'message': self.message,
            'traces': tracelist
        }), self.status_code
