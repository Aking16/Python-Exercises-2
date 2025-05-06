def greedy_algorithm(amount, cash):
  remaining = amount
  results = []

  for money in cash:
    if(remaining >= money):
      remaining -= money
      results.append(money)
  
  return results

cash = [50, 25, 10, 5, 2, 1]
amount = 80

result = greedy_algorithm(amount, cash)

print(result)