def count_positives_sum_negatives(arr):
    if not arr:
        return []
        plus1 = 0
        minus1 = 0
        for n in arr:
            if n > 0:
                plus1 = plus1 + 1
            else:
                minus1 = minus1 + n
        return [plus1, minus1]