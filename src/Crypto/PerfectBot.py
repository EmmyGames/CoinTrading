# This is an unrealistic program that uses future information
# which would not be available, in order to make informed
# decisions on buying or selling with all the current funds.
# It also uses large percent changes to exhaust this point
# This is the maximum possible profit from the sample prices
# We will aim to come as close to this outcome as possible
# without running too low on either type of currency.

# wallet is LTC, USD
wallet = [0, 1000]
# -------------- B   H   H   S   H   H   H  B   S  H  B
samplePrices = [10, 11, 12, 14, 13, 12, 10, 9, 11, 8, 7, 10]
# -------------- B   S   S   S   B   B   B  B   S  B  B


def get_price():
    for i in range(0, len(samplePrices)-1):
        buy_or_sell(samplePrices[i], samplePrices[i+1])
    check_end_value(samplePrices[-1])


def buy_or_sell(price, future_price):
    if price < future_price:
        buy(price)
    elif price > future_price:
        sell(price)


def buy(price):
    wallet[0] += wallet[1] / price
    wallet[1] = 0


def sell(price):
    wallet[1] += wallet[0] * price
    wallet[0] = 0


def check_end_value(price):
    print(wallet[0] * price + wallet[1])
    print(wallet[0])
    print(wallet[1])


if __name__ == '__main__':
    get_price()
