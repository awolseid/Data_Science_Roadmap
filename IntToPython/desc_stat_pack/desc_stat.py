def mean(values):
    if not values:
        return "No input values!"
    return sum(values) / len(values)


def median(values):
    if not values:
        return "No input values!"
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 0:
        mid_value_1 = sorted_values[n / 2]
        mid_value_2 = sorted_values[(n / 2) + 1]
        return (mid_value_1 + mid_value_1) / 2
    else:
        return sorted_values[int((n+1)/2)]


def variance(values, population = True):
    if not values:
        return "No input values!"
    average = mean(values)
    sum_squares = sum((value - average) ** 2 for value in values)
    denom = len(values) if population else (len(values) - 1)
    return sum_squares / denom
