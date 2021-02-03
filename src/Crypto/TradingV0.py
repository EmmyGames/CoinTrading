import matplotlib.pyplot as plt

# wallet is LTC, USD
wallet = [0, 1000]
# average prices is average price, total amount
average_buy_price = [0, 0]
average_sell_price = [0, 0]
# % change needed to buy / sell
volatility = 1.05
fee = 1.005
# This is the % each trade will use from the wallet
risk = 0.5

# -------------- B   H   H   S   H   H   H  B   S  H  B
samplePrices = [10, 11, 12, 14, 13, 12, 10, 9, 11, 8, 7, 10]
# -------------- B   S   S   S   S   S   B  B   S  B  B   S
# -------------- B   S   0   0   0   0   B  0   S  B  0   S

# lists for plot
plot_x = []
plot_y = []


def get_price():
    buy(samplePrices[0])
    for i in samplePrices:
        plot_x.append(i/average_buy_price[0])
        plot_y.append(wallet[0] * i / (wallet[0] * i + wallet[1]) * 100)
        buy_or_sell(i)
        check_end_value(i)


def buy_or_sell(price):
    if price >= average_buy_price[0] * volatility * fee:
        sell(price)
    elif price <= average_sell_price[0] / volatility / fee or price <= average_buy_price[0] / volatility / fee:
        buy(price)


def buy(price):
    # add LTC to wallet by USD/price/fee * risk
    wallet[0] += wallet[1] / price / fee * risk
    # average buy price = avg price * LTC volume + additional USD spent / (LTC volume + additional LTC volume)
    average_buy_price[0] = (average_buy_price[0] * average_buy_price[1] + wallet[1] * risk) / (
            average_buy_price[1] + wallet[1] / price / fee * risk)
    average_buy_price[1] += wallet[0]
    wallet[1] -= wallet[1] * risk
    print("Tried to buy at " + str(price) + " average buy is now " + str(average_buy_price[0]))


def sell(price):
    # add USD to wallet by LTC * price / fee * risk
    wallet[1] += wallet[0] * price / fee * risk
    # average sell price = avg price * LTC volume + USD received / (LTC volume + additional LTC volume sold)
    average_sell_price[0] = (average_sell_price[0] * average_sell_price[1] + wallet[0] * price / fee * risk) / (
                average_sell_price[1] + wallet[0] * risk)
    average_sell_price[1] += wallet[0]
    wallet[0] -= wallet[0] * risk
    print("Tried to sell at " + str(price) + " average sell is now " + str(average_sell_price[0]))


def check_end_value(price):
    print(str(wallet[0]) + " " + str(wallet[1]))
    print(wallet[0] * 10 + wallet[1])


if __name__ == '__main__':
    get_price()
    plt.plot(plot_x, plot_y)
    plt.xlabel("Price / Average Buy Price")
    plt.ylabel('Percent wallet in Crypto')
    plt.show()
