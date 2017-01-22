# steam_transactions

Given the HTML from the steam transaction page is blocked behind account details page, create a data file of each transaction and display a stream of stats for how much you have spent on wallet buys, market transactions (could use steam API for this probably) and how much you truly bought for your games on a yearly basis.

Not really meant to be used for others, but if someone wants to use it for their own use go ahead

To run, you must go into chrome developer tools and firefox dev tools when on the "Transaction History" page (https://store.steampowered.com/account/history/) and copy the full html into a file called transactions.html (don't use "View Page Source" will not give full list, must do copy->outerHtml to get everything).  Run steam.py, which will create steam.json and then run output_steam_stats.py.

    pip install -r requirements.txt
    python steam.py
    python output_steam_stats.py

