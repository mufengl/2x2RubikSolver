from rubik import cubes
from output import input_processor, output_processor

# getting input
cube_input = input_processor()

# processing input
c = cubes(cube_input)

# solve
steps = c.solve()
# print solution (if possible)
if not steps:
    print("Cube was not solved successfully, please verify input")
else:
    input_list = output_processor(steps)
    if len(input_list) == 0:
        print("Cube is already solved")
    for x in range(len(input_list)):
        print(x, end=" ")

#    YY
#    YY
#    BB
#    BB
# OO WW RR
# OO WW RR
#    GG
#    GG
