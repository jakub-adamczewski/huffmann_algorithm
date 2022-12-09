def reverse_keys_with_values(data: dict):
    result = {}
    for k, v in data.items():
        result[v] = k
    return result
