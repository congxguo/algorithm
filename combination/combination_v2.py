def combinate(arr, n):
    final_result = []
    do_combination(arr, 0, n, [], final_result)
    print(f'final_result={final_result}')
    return final_result


def do_combination(arr, start, n, path, final_result):
    # If we have selected n elements → save
    if n == 0:
        final_result.append(path.copy())
        return

    # # If not enough elements left → prune
    if start + n > len(arr):
        return

    # Option 1: take arr[start]
    path.append(arr[start])
    do_combination(arr, start + 1, n - 1, path, final_result)
    path.pop()

    # Option 2: skip arr[start]
    do_combination(arr, start + 1, n, path, final_result)


combinate([1, 2, 3, 6, 8, 9], 4)