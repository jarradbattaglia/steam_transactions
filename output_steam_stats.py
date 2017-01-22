import json
from datetime import datetime

with open("steam.json") as steam:
    steam_data = json.load(steam)

transactions_by_year = {}

class Transaction():
    def __init__(self, date, games_list, price):
        self.date = date
        (self.day, self.month, self.year) = self.parse_year()
        self.games = games_list
        self.price = float(price.replace("$", "").strip())
        self.is_a_market_transaction = False
        self.is_wallet_transaction = False
        for game in self.games:
            if "Key" in game or "Steam Community Market" in game:
                self.is_a_market_transaction = True
                break
            if "Wallet Credit" in game:
                self.is_wallet_transaction = True
                break
    def parse_year(self):
        datetime_obj = datetime.strptime(self.date, "%b %d, %Y")
        return (datetime_obj.day, datetime_obj.month, datetime_obj.year)

    def __str__(self):
        return "(date: %s) (games: %s) (price: %s)" % (self.date, self.games, self.price)
for transaction in steam_data:
    transaction = Transaction(transaction["date"], transaction["games_bought"], transaction["price_total"])
    if transaction.year not in transactions_by_year:
        transactions_by_year[transaction.year] = []
    transactions_by_year[transaction.year].append(transaction)




total_steam_cost = 0
total_steam_games = 0
total_market_transactions = 0
total_market_cost = 0
total_wallet_buys = 0
total_wallet_cost = 0
cum_steam_transactions = 0
cum_steam_cost = 0
for year in sorted(transactions_by_year):
    total_spent_games = 0
    total_spent_market = 0
    total_games = 0
    total_market = 0
    year_wallet_buys = 0
    year_wallet_cost = 0
    for transaction in transactions_by_year[year]:
        if transaction.is_a_market_transaction:
            total_spent_market += transaction.price
            total_market += 1
        elif transaction.is_wallet_transaction:
            year_wallet_buys += 1
            year_wallet_cost += transaction.price
        else:
            total_spent_games += transaction.price
            total_games += len(transaction.games)
    print "For year %s, you bought %d games for $%f" % (year, total_games, total_spent_games)
    print "Keys bought %s for $%s" % (total_market, total_spent_market)
    print "Wallet transactions %s for $%s" % (year_wallet_buys, year_wallet_cost)
    total_steam_cost += total_spent_games
    total_steam_games += total_games
    total_wallet_buys += year_wallet_buys
    total_wallet_cost += year_wallet_cost
    total_market_cost += total_spent_market
    total_market_transactions += total_market


print "Steam Games: %s with a total cost of $%s" % (total_steam_games, total_steam_cost)
print "Keys bought: %s with a total cost of $%s" % (total_market_transactions, total_market_cost)
print "Wallet buys: %s with a total cost of $%s" % (total_wallet_buys, total_wallet_cost)

cum_steam_transactions = total_wallet_buys + total_steam_games + total_market_transactions
cum_steam_cost = total_steam_cost + total_market_cost + total_wallet_cost
print "Total Transactions: %s and Total Cost: %s" % (cum_steam_transactions, cum_steam_cost)
print cum_steam_cost / 8