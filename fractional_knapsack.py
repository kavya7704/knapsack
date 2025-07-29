def sort_by_value(item):
    return item[0]

def sort_by_weight(item):
    return item[1]

def sort_by_ratio(item):
    return item[0] / item[1]

def fractional_knapsack(W, items, strategy='ratio'):
    if strategy == 'value':
        items.sort(key=sort_by_value, reverse=True)
    elif strategy == 'weight':
        items.sort(key=sort_by_weight)  # ascending order
    elif strategy == 'ratio':
        items.sort(key=sort_by_ratio, reverse=True)
        
    total_value = 0.0
    result_items = []

    for value, weight in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
            result_items.append((value, weight, 1.0))
        else:
            fraction = W / weight
            total_value += value * fraction
            result_items.append((value, weight, fraction))
            W = 0
            break

    return total_value, result_items

# Test case
W = 15
items = [(5,1),(10,3),(7,4),(8,1),(9,3),(4,2)]

print(fractional_knapsack(W, items.copy(), 'value'))
print(fractional_knapsack(W, items.copy(), 'weight'))
print(fractional_knapsack(W, items.copy(), 'ratio'))
