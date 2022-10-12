import requests
import sys
import json

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            num = float(sys.argv[1])
            current_cost = get_price(num)
            print(current_cost)
        except ValueError:
            sys.exit("Command-line argument is not a number")


def get_price(n):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        price = o["bpi"]["USD"]["rate_float"]
        # print(json.dumps(response.json(), indent=2))
        # print("USD price:", price)
        total = float(price) * n
        formatted_total = "${:,.4f}".format(total)
        return formatted_total
    except requests.RequestException:
        pass

if __name__ == "__main__":
    main()
