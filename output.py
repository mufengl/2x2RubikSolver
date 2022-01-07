from collections import Counter


def input_processor():
    cube_input = ""
    print("Start with the front side facing you, enter the following:")
    color = True
    while len(cube_input) != 24 or not color:
        top = input("The colors on the topside going from left to right, top to bottom:")
        front = input("Now the colors on the front side:")
        left = input("Now the colors on the left side:")
        right = input("Now the colors on the right side:")
        bot = input("Now the colors on the bottom:")
        back = input("Finally the colors on the back (with the front facing you"
                     + " rotate the cube 180 degrees with respect to the vertical axis):")

        cube_input = top + front + left[1] + left[3] + bot[:2] + right[0] + right[2] + left[0] + left[2] + bot[:-2] + \
                     right[3] + right[1] + back[::-1]

        num_colors = Counter(cube_input)

        for x in ['Y', 'W', 'G', 'B', 'R', 'O']:
            if num_colors[x] != 4:
                color = False

        if len(cube_input) != 24:
            print("Invalid cube, please verify input: ")

    return cube_input


def output_processor(moves_input):
    input_list = moves_input.split(" ")
    input_list.pop(-1)

    repeats = []
    opposites = []
    i = 0
    while i < len(input_list) - 2:
        if input_list[i] == input_list[i + 1] and input_list[i + 1] == input_list[i + 2]:
            input_list.insert(i, input_list[i] + "'")
            for x in range(3):
                input_list.pop(i + 1)
        i += 1

    for x in range(len(input_list) - 1):
        if input_list[x] == input_list[x + 1]:
            input_list[x] = input_list[x] + "2"
            repeats.append(x + 1)

    for x in range(len(repeats), 0, -1):
        input_list.pop(repeats[x - 1])

    for x in range(len(input_list) - 1):
        if input_list[x][: 1] + "'" == input_list[x + 1] or input_list[x] == input_list[x + 1][: 1] + "'":
            opposites.append(x + 1)

    for x in range(len(opposites), 0, -1):
        input_list.pop(opposites[x - 1])
        input_list.pop(opposites[x - 1] - 1)

    return input_list
