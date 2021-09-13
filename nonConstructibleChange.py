def nonConstructibleChange(coins):
    coins.sort()
    prev_sum = 0
    for coin in coins:
        if coin > prev_sum + 1:
            return prev_sum + 1
        prev_sum += coin
    return prev_sum
