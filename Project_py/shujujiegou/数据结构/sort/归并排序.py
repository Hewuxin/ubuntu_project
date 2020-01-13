# 时间复杂度 O（nlogn）
# 稳定性稳定


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res


if __name__ == "__main__":
    print(merge_sort([1, 2, 5, 4, 3, 10, 6, 15, 9]))
