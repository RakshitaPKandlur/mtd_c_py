
n, p = map(int, input("Enter n and p: ").split())  
prices = list(map(int, input("Enter prices: ").split()))  

def earnings(n, p, prices):
    negative_prices = sorted(filter(lambda x: x < 0, prices)) 
    return abs(sum(negative_prices[:p]))  

print(earnings(n, p, prices))

