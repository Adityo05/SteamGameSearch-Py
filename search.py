def binary_search(arr, left, right, x, key):
    results = []
    x = x.lower()
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = str(arr[mid][key]).lower()
        if x in mid_value:
            start, end = mid, mid
            while start > left and x in str(arr[start - 1][key]).lower():
                start -= 1
            while end < right and x in str(arr[end + 1][key]).lower():
                end += 1
            for i in range(start, end + 1):
                if x in str(arr[i][key]).lower():
                    results.append(arr[i])
            break
        elif x < mid_value:
            right = mid - 1
        else:
            left = mid + 1
    return results

def exponential_search(data, x, key):
    data.sort(key=lambda k: str(k.get(key, '')).lower())
    n = len(data)
    x = x.lower()
    results = []
    if x in str(data[0][key]).lower():
        results.append(data[0])
    i = 1
    while i < n and str(data[i][key]).lower() <= x:
        i *= 2
    results.extend(binary_search(data, i // 2, min(i, n - 1), x, key))
    for item in data:
        if x in str(item[key]).lower() and item not in results:
            results.append(item)
    return results
