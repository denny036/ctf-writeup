def has_ones_digit_3(num):
    return num % 10 == 3 or num % 3 == 0

def produce_3s(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        result = ['N'] * n

        for i in range(n):
            if has_ones_digit_3(a[i]):
                result[i] = 'Y'
            for j in range(i):
                if result[j] == 'Y' and has_ones_digit_3(a[i] * a[j]):
                    result[i] = 'Y'
                    break

        print(''.join(result))

# Sample Input
t = 2
test_cases = [
    (10, [5, 2, 9, 8, 3, 7, 6, 1, 4, 10]),
    (5, [3, 7, 2, 7, 7])
]

# Function Call
produce_3s(t, test_cases)
