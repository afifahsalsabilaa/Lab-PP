input()
candles = list(map(int, input().split(" ")))

max_candles= max(candles)
count_max_candles= 0

for i in candles:
    if i == max_candles:
        count_max_candles += 1                  

print(count_max_candles)