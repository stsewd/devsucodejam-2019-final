def lastDigitSort(digits):
    digits = list(map(str, digits))
    digits.sort(key=lambda n: n[::-1])
    return list(map(int, digits))
