numbers = [float(temp) for temp in input("Enter numbers: ").split()]
N = len(numbers)
# print(numbers)


def swap(a, b):
    return b, a


for i in range(N):
    for j in range(N-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = swap(numbers[j], numbers[j+1])

print("Sorted numbers: ", numbers)
