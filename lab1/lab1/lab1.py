RED = '\u001b[41m'
YELLOW = '\u001b[43;1m'
GREEN = '\u001b[42m'
BLACK = '\u001b[16m'
WHITE_BG = '\033[48;5;15m'
END = '\u001b[0m'
ESC = '\x1b'
CSI = f'{ESC}['
RESET = f'{CSI}0m' 

# 1. Флаг

def flag():
    for i in range(6):
        if i < 3:
            print(f'{GREEN}{" " * 9}{YELLOW}{" " * 14}{END}')
        else:
            print(f'{GREEN}{" " * 9}{RED}{" " * 14}{END}')


if __name__ == '__main__':
    flag()

# 2. Узор

def draw_line(line):
    print(line)


def double_rombs(height=11, colour=16, colour1=15):
    center = height // 2

    for i in range(height):
        if i <= center:
            length = 1 + 2 * i
            offset = center - i
        else:
            length = 1 + 2 * (height - i - 1)
            offset = i - center

        if i < center:
            gap = (center - i) * 2 - 3
        elif i == center:
            gap = -1 
        else:
            gap = (i - center) * 2 - 3

        left = f'{CSI}48;5;{colour1}m{" " * offset}{RESET}{CSI}48;5;{colour}m{" " * length}{RESET}'
        middle = "" if gap < 0 else f'{CSI}48;5;{colour1}m{" " * max(0, gap)}'
        right = f'{CSI}48;5;{colour}m{" " * length}{RESET}{CSI}48;5;{colour1}m{" " * offset}{RESET}'
        draw_line(left + middle + right)


if __name__ == "__main__":
    double_rombs()

# 3. График y=x+1

for y in range(10, -2, -1):
    row = ""
    for x in range(-2, 20):
        if x + 1 == y:
            row += "*"
        elif x == 0: 
            row += "|"
        elif y == 0: 
            row += "-"
        else: 
            row += " "
    print(row)

# 4. Диаграмма 

nums = [float(x) for x in open('sequence.txt').read().split()]

group1 = [x for x in nums if x > 0 and x < 5]
group2 = [x for x in nums if x < 0 and x < -5]

total = len(group1) + len(group2)

p1 = len(group1) / len(nums) * 100
p2 = len(group2) / len(nums) * 100

print('от 0 до  5:', '#' * round(p1), f'{len(group1)}/{total}')
print('от 0 до -5:', '#' * round(p2), f'{len(group2)}/{total}')
