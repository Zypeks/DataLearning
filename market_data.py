#  imports

import ccxt
#connector
ku = ccxt.kucoinfutures({
    'EnableRateLimit': True,
    'apiKey': '65945c5bec0a82000192d84b',
    'secret': '9bde49f4-be38-47fe-95fd-07d510f33118',
    'password': 'ziomek21',
})

markets = ku.fetch_markets()
print(markets)

print(ku.fetch_balance())
