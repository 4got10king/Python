import json

import requests

from config import keys


class CovertionException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise CovertionException('equal parameters')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise CovertionException(f'Value "{quote}" not found')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise CovertionException(f'Value "{base}" not found')

        try:
            amount = float(amount)
        except ValueError:
            raise CovertionException(f'Value "{amount}" wrong')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base

