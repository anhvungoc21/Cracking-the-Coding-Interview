# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.

def solution(n):
    denoms = [25, 10, 5, 1]

    # Row: denom, Col: n
    memo = [[0 for _ in range(len(denoms))] for _ in range(n + 1)]

    return coins(n, denoms, 0, memo)

def coins(money, denoms, index, memo):
    # ! These are not Base cases. We're recursing on denoms, not money.
    # if money < 0: return 0
    # if money == 0: return 1

    # Calculated
    if memo[money][index] > 0:
        return memo[money][index]
    
    # Reached last denomination
    if index == len(denoms) - 1:
        return 1 if (money % denoms[index] == 0) else 0
    
    # Recurse
    # ! Trap: Do not recurse on each denom. This creates repetitions.
    # Instead, recurse on using 1...k coins of one denom at a time
    ways = 0
    spend = 0
    while spend <= money:
        ways += coins(money - spend, denoms, index + 1, memo)
        spend += denoms[index]

    # Store result. 
    # Note: This pair of coordinates represent an 
    # ? exisitng amount of money, and the denom taken from it
    memo[money][index] = ways
    return ways

print(solution(10)) 
# 1s
# 5 + 1sw2ww2ss
# 5 + 5
# 10
    