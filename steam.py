from lxml import html
import csv
import re

with open("transactions.html", "r") as st:
    steam = st.read()
tree = html.fromstring(steam)
header_row = tree.xpath("//table/thead/tr/th/text()")
print header_row
elements = tree.xpath("//table/tbody/tr")


for row in elements:
    row_list = [re.sub('[\t\r]', '', text.text_content().strip(" ").strip()) for text in row.xpath("./td")]
    if row:
      games = row_list[1].split("\n")
      for game in games:
        print game.strip().strip("\n")