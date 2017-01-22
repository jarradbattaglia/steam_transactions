from lxml import html
import csv
import re
import json

with open("transactions.html", "r") as st:
    steam = st.read()
tree = html.fromstring(steam)
header_row = tree.xpath("//table/thead/tr/th/text()")
elements = tree.xpath("//table/tbody/tr")

# Print out rows of content
transaction_json = []
for row in elements:
    row_list = [re.sub('[\t\r]', '', text.text_content().strip(" ").strip()) for text in row.xpath("./td")]
    if len(row) > 0:
        date = row_list[0].strip()
        games = [game.strip() for game in row_list[1].split("\n") if game.strip()]
        price_total = row_list[3].split("\n")[0].strip("\t").strip("\n").strip("\r").strip()
        if not games or not price_total:
            continue
        row_transactions = { "date": date, "games_bought": games, "price_total": price_total}
        transaction_json.append(row_transactions)

with open("steam.json", "wb") as steam:
    steam.write(json.dumps(transaction_json, indent=2))

