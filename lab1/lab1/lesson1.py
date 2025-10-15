import time


ESC = '\x1b'
CSI = f'{ESC}['
RESET = f'{CSI}0m'


# def loading():
#     print('loading...')
#     for i  in range(100):
#         print(f'{csi}1G{i + 1}%', end='', flush= True)
#         time.sleep(0.2)


# def show_progress(num_task, width):
#     for task in range(1, num_task + 1):
#         for filled in range(width):
#             bar = f'{'#' * filled}{'-' * (width - filled - 1)}'
#             print(f'{csi}1G{task}/{num_task} {bar}', end="", flush= True)
#             time.sleep(0.2)




def draw_line(offset, length, colour):
    line = f'{' ' * offset}{CSI}48;5;{colour}m{' ' * length}{RESET}'
    print(line)
draw_line(7, 10, 19)

def draw_romb(height=15):
    center = height // 2
    step = 1
    length = 1
    offset = center
    while True:
        for colour in range(16, 232):
            for line in range(height):
                draw_line(offset, length, colour)
                if line < center:
                    offset -= step
                    length += step * 2
                else:
                    offset += 1
                    length -= step * 2
            print(f'{CSI}{height}A{CSI}1G', end='')
            offset = center
            length = 1


# if __name__ == '__main__':
    # show_progress(width = 30, num_task = 3)
    # draw_romb()

