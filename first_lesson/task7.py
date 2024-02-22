values = [12, 134, 10, 47, 100, 20, 50, 160, 210]
tens = list(filter(lambda a: a%10==0, values))
print(tens)