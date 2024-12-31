def knapsack_procedural(capacity, items):

    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            value, weight = items[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    return dp[n][capacity], selected_items

def knapsack_functional(capacity, items):
    def knapsack_recursive(c, i):
        if i == 0 or c == 0:
            return 0, []

        value, weight = items[i - 1]
        if weight > c:
            return knapsack_recursive(c, i - 1)

        without_item = knapsack_recursive(c, i - 1)
        with_item = knapsack_recursive(c - weight, i - 1)
        with_item = (with_item[0] + value, with_item[1] + [items[i - 1]])

        return max(without_item, with_item, key=lambda x: x[0])

    return knapsack_recursive(capacity, len(items))


capacity = 10
items = [
    (60, 2),
    (100, 3),
    (120, 4),
]

print("Proceduralne podejście:")
max_value_proc, selected_items_proc = knapsack_procedural(capacity, items)
print("Maksymalna wartość:", max_value_proc)
print("Wybrane przedmioty:", selected_items_proc)

print("\nFunkcyjne podejście:")
max_value_func, selected_items_func = knapsack_functional(capacity, items)
print("Maksymalna wartość:", max_value_func)
print("Wybrane przedmioty:", selected_items_func)
