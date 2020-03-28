import json, urllib.request, os, time

#url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc'

url = 'https://api.coingecko.com/api/v3/coins/bitcoin'
data = urllib.request.urlopen(url).read().decode()
data_obj = json.loads(data)
dash = '-' * 60

while(True):
    os.system('clear')
    print(dash)
    print('CRYPTO PRICE MONITOR')
    print(dash)

    header = ['name', 'price', 'market cap', '24h change']
    print('{:<12s}{:<10s}{:<20s}{:<10s}'.format(header[0], header[1], header[2], header[3]))



    print('{:<12s}'.format(data_obj['id']) + '$', end= '')
    print('{:<9s}'.format(str(data_obj['market_data']['current_price']['usd'])), end='')
    print('{:<19s}'.format('{:,}'.format(data_obj['market_data']['market_cap']['usd'])), end='')
    print('{:<10s}'.format(str(data_obj['market_data']['price_change_percentage_24h'])))
    time.sleep(600)


