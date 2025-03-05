"""In a file called bitcoin.py, implement a program that:
-Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If 
that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
-Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which 
returns a JSON object, among whose nested keys is the current price of Bitcoin as a float."""

import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    f = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

dict = response.json()
bitcoin = dict["bpi"]["USD"]["rate_float"]
amount = bitcoin * f
print(f"${amount:,.4f}")