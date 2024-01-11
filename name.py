import sys

# name = input('Как тебя зовут?\n')
name = sys.stdin.readline().rstrip()
print(f'Привет, {name}!')
