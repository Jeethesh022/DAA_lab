import random

comparison_count = 0

def min_max_dc(arr, low, high):
    global comparison_count

    
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    
    mid = (low + high) // 2

    
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


def min_max_native(arr):
    mn = mx = arr[0]
    comps = 0

    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x

        comps += 1
        if x > mx:
            mx = x

    return mn, mx, comps



arr = [3, 1, 7, 4, 2, 8, 5, 6, 0]

comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comparisons = comparison_count

_, _, naive_comps = min_max_native(arr)

print("Sample Array")
print(f"Array: {arr}")
print(f"Minimum: {mn}")
print(f"Maximum: {mx}")
print(f"Divide & Conquer Comparisons: {dc_comparisons}")
print(f"Naive Comparisons: {naive_comps}")


print("\n{:>8} {:>12} {:>15} {:>18}".format(
    "Size", "D&C", "Naive", "3n/2 - 2"))
print("-" * 58)

for size in [10, 100, 1000, 10000]:
    arr = [random.randint(1, 10000) for _ in range(size)]

    comparison_count = 0
    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc = comparison_count

    _, _, naive = min_max_native(arr)

    formula = 3 * size / 2 - 2

    print("{:>8} {:>12} {:>15} {:>18.1f}".format(
        size, dc, naive, formula))

