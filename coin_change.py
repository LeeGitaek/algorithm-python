n = 1260
coin_count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    if n%coin != 0:
        coin_count += n/coin
        n %= coin

print(int(coin_count))
