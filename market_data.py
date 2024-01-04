#  imports
import json
import numpy as np
from datetime import date, datetime, tzinfo
import pandas as pd
import time, schedule, random
import ccxt
#connector
ku = ccxt.kucoinfutures({
    'EnableRateLimit': True,
    'apiKey': '65945c5bec0a82000192d84b',
    'secret': '9bde49f4-be38-47fe-95fd-07d510f33118',
    'password': 'ziomek21',
})
params = {'future' : True}
markets = ku.fetch_markets(params=params)
#print(markets)
symbols_df = pd.DataFrame()
temp_df = pd.DataFrame()
time.sleep(8877)
for n in markets: 
    sym = n['id']
    #print(sym)
    temp_df['symbol'] = [sym]
    print('-')
    symbols_df = symbols_df.append(temp_df)
print(symbols_df)
symbols_df.to_csv('ku_symbols.csv', index=False)
time.sleep(7834)

# index position of symbol
all_symbols = pd.read_csv('ku_symbol')
random_symbol_pos = random.randrange(0,6)
random_symbol = all_symbols.iloc[random_symbol_pos ['symbol']]
symbols = all_symbols['symbol'].values.tolist()
symbol = random_symbol
print(symbols,symbol,ra)