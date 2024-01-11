import sys


def main():
    elements_count = int(sys.stdin.readline().rstrip())
    data = (list(map(int, input().split())))
    unique_data = list(set(data))
    unique_data.sort()
    duplicate_count = len(data) - len(unique_data)

    if duplicate_count > 0:
        while len(unique_data) < elements_count:
            unique_data.append('_')
    print(*unique_data)


if __name__ == '__main__':
    main()
