import random
import graphics

global XCordinate
global YCordinate
global graphwin
row = 7
column = 7
matrix_1 = []
matrix_2 = []


class node:
    val = 0

    def __init__(self, val):
        self.val = val


def functionMatrixPrint(matrix_1):
    for lines in range(0, row):
        for line in range(0, column):
            elements = matrix_1[lines][line]
            print(elements.val, ' ', end='')
        print()


def setCoordinate(matrix_1, cor1, cor2):
    matrix_1[cor1][cor2].val = 3
    x = max(cor1 - 3, 0)
    while x < cor1 + 3 and x < row:
        y = max(cor2 - 3, 0)
        while y < cor2 + 3 and y < column:
            matrix_1[x][y].val = max(matrix_1[x][y].val, 3 - max(max(y - cor2, cor2 - y), max(x - cor1, cor1 - x)))
            y = y + 1
        x = x + 1


def matObj(matrix_2):
    for lines in range(0, row):
        for line in range(0, column):
            point1 = graphics.Point((lines * 50) + 60, (line * 50) + 60)
            point2 = graphics.Point((lines * 50) + 100, (line * 50) + 100)
            rect = graphics.Rectangle(point1, point2)
            rect.setFill('white')
            rect.draw(graphwin)

    for lines in range(0, row):
        point1 = graphics.Point((lines * 50) + 70, 40)
        label = graphics.Text(point1, lines)
        label.setTextColor('white')
        label.draw(graphwin)
        
    for line in range(0, column):
        point1 = graphics.Point(40, (line * 50) + 70)
        label = graphics.Text(point1, line)
        label.setTextColor('white')
        label.draw(graphwin)
        
    for scale in range(0, 4):
        txt = graphics.Point((scale * 50) + 130, (column * 50) + 100)
        point1 = graphics.Point((scale * 50) + 110, (column * 50) + 110)
        point2 = graphics.Point((scale * 50) + 150, (column * 50) + 150)
        rect = graphics.Rectangle(point1, point2)

        if scale == 3:
            label = graphics.Text(txt, "High")
            label.setTextColor('white')
            label.draw(graphwin)
            rect.setFill('Red')
        elif scale == 2:
            rect.setFill('Orange')
        elif scale == 1:
            rect.setFill('Yellow')
        elif scale == 0:
            label = graphics.Text(txt, "Low")
            label.setTextColor('white')
            label.draw(graphwin)
            rect.setFill('Green')
        rect.draw(graphwin)


def draw_objects(matrix_2):
    for lines in range(0, row):
        for line in range(0, column):
            if matrix_2[lines][line].val == 3:
                graphwin.items[lines * row + line].setFill('Red')
            elif matrix_2[lines][line].val == 2:
                graphwin.items[lines * row + line].setFill('Orange')
            elif matrix_2[lines][line].val == 1:
                graphwin.items[lines * row + line].setFill('Yellow')
            elif matrix_2[lines][line].val == 0:
                graphwin.items[lines * row + line].setFill('Green')
            graphwin.update()



XCordinate = row * 50 + 100
YCordinate = column * 50 + 200
graphwin = graphics.GraphWin("Display", XCordinate, YCordinate)
graphwin.setBackground('black')

for l in range(0, row):
    row1 = []
    row2 = []
    for m in range(0, column):
        node1 = node(0)
        node2 = node("-")
        row1.append(node1)
        row2.append(node2)

    matrix_1.append(row1)
    matrix_2.append(row2)

for l in range(0, int((random.random() * 3)) + 1):
    x1 = int(1 + (random.random() * (row - 2)))
    y1 = int(1 + (random.random() * (column - 2)))

    setCoordinate(matrix_1, x1, y1)

matObj(matrix_2)

while True:
    onMouse = graphwin.getMouse()
    getx = onMouse.getX() - 50
    getx /= 50
    gety = onMouse.getY() - 50
    gety /= 50
    getx = int(getx)
    gety = int(gety)

    print("Guess x: ", getx, "guess y: ", gety)
    matrix_2[getx][gety] = matrix_1[getx][gety]
    value = matrix_1[getx][gety].val
    draw_objects(matrix_2)

    if int(value) == int(3):
        break
    functionMatrixPrint(matrix_2)

print("\nYou win!!!")
functionMatrixPrint(matrix_1)
draw_objects(matrix_1)