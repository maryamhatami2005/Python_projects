import requests
from cachetools import cached, TTLCache
import time

cache = TTLCache(maxsize= 100, ttl= 3*60*60)

@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    time.sleep(2)
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][target_currency]


def conventor_currency(base_currency_amount, exchange_rate):
    return base_currency_amount * exchange_rate

if __name__=="__main__":
    base = input("Enter base currency: ")
    target = input("Enter target currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(base, target)
    converted_amount = conventor_currency(amount, exchange_rate)
    print(f"{amount} {base} is {converted_amount} {target}")