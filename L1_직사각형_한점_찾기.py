def solution(v):
    x_coords = [v[0][0], v[1][0], v[2][0]]
    y_coords = [v[0][1], v[1][1], v[2][1]]

    # x좌표 구하기
    if x_coords.count(x_coords[0]) == 1:
        x4 = x_coords[0]
    elif x_coords.count(x_coords[1]) == 1:
        x4 = x_coords[1]
    else:
        x4 = x_coords[2]

    # y좌표 구하기
    if y_coords.count(y_coords[0]) == 1:
        y4 = y_coords[0]
    elif y_coords.count(y_coords[1]) == 1:
        y4 = y_coords[1]
    else:
        y4 = y_coords[2]

    return [x4, y4]
