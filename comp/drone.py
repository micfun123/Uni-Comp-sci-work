inputs = int(input())
finish_list = []
control_list = []

for i in range (inputs):
    control_list.append(input())

for i in range (inputs):
    control = control_list[i]
    control = control.split()

    pitch = int(control[0])
    roll = int(control[1])
    yaw = int(control[2])

    if pitch != 0 and roll == 0:
        north = 0.0 + yaw / 2
        east = 0.0 + pitch / 2
        south = 0.0 + yaw / 2
        west = 0.0 - pitch / 2

    elif roll != 0 and pitch == 0:
        north = 0.0 + roll / 2
        east = 0.0 + yaw / 2
        south = 0.0 - roll / 2
        west = 0.0 + yaw / 2

    else:
        north = 0.0 + roll/2 + yaw/4
        east = 0.0 + pitch/2 + yaw/4
        south = 0.0 - roll/2 + yaw/4
        west = 0.0 - pitch/2 + yaw/4


    print(north," " ,east, " ",south, " ",west)