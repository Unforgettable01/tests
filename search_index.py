import sys


def main():
    sort_numbers = list(map(int, sys.stdin.readline().split()))
    element = int(sys.stdin.readline())
    left = 0
    right = len(sort_numbers) - 1
    mid = 0

    if sort_numbers[left] >= element:
        return left
    if sort_numbers[right] < element:
        return right + 1

    while left < right:
        mid = (left + right) // 2
        if sort_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
        if sort_numbers[mid] == element:
            return mid

    if element < sort_numbers[mid]:
        return mid

    return mid + 1


if __name__ == '__main__':
    print(main())
